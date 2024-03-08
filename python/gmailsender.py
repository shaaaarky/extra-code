import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(sender, to, subject, file):
    
    # Filling out password with getpass module
    print(f"From: {sender} To: {to}")
    password = "xinj etds egpz whlj"

    
    # Zip handling
    #z = MIMEMultipart(f"{file}", "zip")
    #z.set_payload(zipfile.ZipFile(file=file, mode="r"))
    # Message
    
    msg = MIMEMultipart()
    msg["subject"] = subject
    msg["To"] = to
    msg["From"] = sender
    
    
    attachment = MIMEText("Zip files in python")
    attachment.add_header('Content-Disposition', 'attachment', filename=file)
    
    msg.attach(MIMEText(open(file).read()))

    print("File successfully attached")


    # Logging in and sending email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:

        # Logging in to smtp instance
        status_code, response = smtp_server.login(sender, password)
        print(f"[*] Logging in: {status_code} {response}")

        # Sending email
        smtp_server.sendmail(sender, to, msg.as_string())
        smtp_server.close()
    print("Email sent successfully")
    
    # Sending email

user = os.getlogin()
# os.chdir(f"C:\\Users\\{user}\\Desktop\\ziptesting")

body = "Repeated function in python"
subject = 'Emails with python'
to = 'benwellington685@gmail.com'
sender = 'bradshawcantos@gmail.com'
user = 'benwellington685@gmail.com'
file = "C:\\Users\\JohnBradshawCantos\\Documents\\log.txt"

sendmail(sender=sender, to=to, subject=subject, file=file)
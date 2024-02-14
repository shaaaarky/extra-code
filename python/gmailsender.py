import os
import getpass
import smtplib
import zipfile
import tempfile
from email import encoders
from email.message import Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def sendmail(sender, to, subject, body, file):
    
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
    msg.attach(attachment)



    # Logging in and sending email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:

        # Logging in to smtp instance
        status_code, response = smtp_server.login(sender, password)
        print(f"[*] Logging in: {status_code} {response}")

        # Sending email
        smtp_server.sendmail(sender, to, msg.as_string())

    print("Email sent")
    
    # Sending email
    # smtpserver.sendmail(sender, to, message)
    # smtpserver.close()


user = os.getlogin()
# os.chdir(f"C:\\Users\\{user}\\Desktop\\ziptesting")

body = "Repeated function in python"
subject = 'Emails with python'
to = 'benwellington685@gmail.com'
sender = 'bradshawcantos@gmail.com'
user = 'benwellington685@gmail.com'

sendmail(sender=sender, to=to, subject=subject, body=body, file=f"C:\\Users\\JohnBradshawCantos\\Desktop\\ziptesting.zip")
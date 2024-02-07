import getpass
import smtplib
from email.mime.text import MIMEText



def sendmail(sender, to, user, subject, body):
    
    # Message
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg[]
    
    
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       print(f"[*] Logging in: {status_code} {response}")
       smtp_server.sendmail(sender, recipients, msg.as_string())
    
    # Prints detes of connection and prompts the user for a password
    print(f"From: {sender} To: {to}")
    password = getpass.getpass("Password: ")

    # SMTP extented hello
    status_code, response = smtpserver.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    # Start of TLS instance
    status_code, response = smtpserver.starttls()
    print(f"[*] Starting TLS Connection: {status_code} {response}") 

    # Login to server 
    smtpserver.login(user, password)
    

    
    
    # Sending email
    # smtpserver.sendmail(sender, to, message)
    # smtpserver.close()


body = "Repeated function in python"
subject = 'Emails with python'
to = 'bradshawcantos@gmail.com'
sender = 'bradshawcantos@outlook.com'
user = 'bradshawcantos@outlook.com'
sendmail(sender=sender, to=to, user=user, subject=subject, body=body)
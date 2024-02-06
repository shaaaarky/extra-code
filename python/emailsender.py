import getpass
import smtplib

def sendmail(sender, to, user, subject, body):
    # Detes to fill out  
    
    smtpserver = smtplib.SMTP("smtp-mail.outlook.com", 587)
    
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
    print(f"[*] Logging in: {status_code} {response}")

    header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
    message = header + '\n' + body
    
    # Sending email
    smtpserver.sendmail(sender, to, message)
    smtpserver.close()

t = "Repeated function in python"
subject = 'Emails with python'
to = 'bradshawcantos@gmail.com'
sender = 'bradshawcantos@outlook.com'
user = 'bradshawcantos@outlook.com'
sendmail(sender=sender, to=to, user=user, subject=subject, body=t)
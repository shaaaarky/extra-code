import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "bradshawcantos@outlook.com"
TO_EMAIL = "benwellington685@gmail.com"
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: Python
Hello! This is an automated message sent by a python script

"""

smtp = smtplib.SMTP(HOST, PORT)
status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS Connection: {status_code} {response}") 

status_code, response = smtp.login(FROM_EMAIL, TO_EMAIL)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()


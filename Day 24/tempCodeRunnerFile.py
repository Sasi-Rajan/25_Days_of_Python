from tkinter import *
ENTRY_FONT=("Arial",12)
LABEL_FONT=("Arial",12,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open ("password.txt") as password_file:
        password_file.write("Hello")
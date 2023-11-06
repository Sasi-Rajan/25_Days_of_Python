from tkinter import *
from tkinter import messagebox
from password_generator import generate
import pyperclip
ENTRY_FONT=("Arial",12)
LABEL_FONT=("Arial",12,"bold")

#PASSWORD GENERATOR
def random_password_generator():
    password=generate()
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
    

#SAVE PASSWORD
def save_password():
    website=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    if len(website) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail\\Username: {username} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open ("password.txt","a") as password_file:
                password_file.write(f"website : {website} | Username : {username} | Password : {password}\n")
            website_entry.delete(0,"end")
            password_entry.delete(0,"end")
    else:
        messagebox.showinfo(title="Missing Credentials",message="Dont leave any fields empty")
#UI SETUP
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")



canvas=Canvas(window,width=200,height=200,bg="white",highlightthickness=0)
photo=PhotoImage(file="logo_revised.png")
canvas.create_image(200//2,200//2,image=photo)
canvas.grid(row=0,column=1)


website_label=Label(window,text="Website:",font=LABEL_FONT,bg="white",fg="black")
website_label.grid(row=1,column=0,padx=4,pady=6)

website_entry=Entry(window,width=35,bg="white",fg="black",font=ENTRY_FONT,borderwidth=2)
website_entry.grid(row=1,column=1,columnspan=2,padx=4,pady=6)
website_entry.focus()


username_label=Label(window,text="Email/Username:",font=LABEL_FONT,bg="white",fg="black")
username_label.grid(row=2,column=0,padx=4,pady=6)


username_entry=Entry(window,width=35,bg="white",fg="black",font=ENTRY_FONT,borderwidth=2)
username_entry.grid(row=2,column=1,columnspan=2,padx=4,pady=6)
username_entry.insert(0, "mailbox.sasiraj@gmail.com")


password_label=Label(window,text="Password:",font=LABEL_FONT,bg="white",fg="black")
password_label.grid(row=3,column=0,padx=4,pady=6)


password_entry=Entry(window,width=21,bg="white",fg="black",font=ENTRY_FONT,borderwidth=2)
password_entry.grid(row=3,column=1,padx=4,pady=6)



generate_password_button=Button(text="Generate Password",bg="white",fg="black",command=random_password_generator)
generate_password_button.grid(row=3,column=2,padx=4,pady=6)



add_button=Button(text="Add",width=44,bg="white",fg="black",command=save_password)
add_button.grid(row=4,column=1,columnspan=2,padx=4,pady=6)



window.mainloop()
from tkinter import *


#Window setup
window=Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg='90c2ae')


#Photo Image
front_image=PhotoImage(file=r"images\card_front.png")
back_image=PhotoImage(file=r"images\card_back.png")
right=PhotoImage(file=r"images\right.png")
wrong=PhotoImage(file=r"images\wrong.png")




#UI Setup

canvas=Canvas(window,width=800,height=526)
canvas.create_image(400,263,image=front_image)
canvas.pack()





window.mainloop()
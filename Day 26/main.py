from tkinter import *
import pandas as pd
import random
current_card={}
learn={}
try:
    language_file=pd.read_csv("Words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("japanese_to_english.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn=language_file.to_dict(orient="records")

def next_card():
    global current_card , flip_time
    window.after_cancel(flip_time)
    current_card=random.choice(learn)
    canvas.itemconfig(card_title,text="Japanese",fill="black")
    canvas.itemconfig(card_word,text=current_card["Japanese"],fill="black")    
    canvas.itemconfig(card_background,image=front_image)
    flip_time=window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_image)

def remove_card():
    learn.remove(current_card)
    data=pd.DataFrame(learn)
    data.to_csv("Words_to_learn.csv",index=False)
    next_card()

    
#Window setup
window=Tk()
window.title("Flash Cards")
window.config(padx=30,pady=30,bg="#90c2ae")

flip_time=window.after(3000,func=flip_card)



#Photo Image
front_image=PhotoImage(file=r"images\card_front.png")
back_image=PhotoImage(file=r"images\card_back.png")
right_image=PhotoImage(file=r"images\right.png")
wrong_image=PhotoImage(file=r"images\wrong.png")




#UI Setup

canvas=Canvas(window,width=800,height=450,highlightthickness=0,bg="#90c2ae")
card_background=canvas.create_image(400,450//2,image=front_image)
canvas.grid(row=0,column=0,columnspan=2)


card_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,300,text="Word",font=("Arial",60,"bold"))

wrong_button=Button(image=wrong_image,highlightthickness=0,bg="#90c2ae",command=next_card)
wrong_button.grid(row=1,column=0)

right_button=Button(image=right_image,highlightthickness=0,bg="#90c2ae",command=remove_card)
right_button.grid(row=1,column=1)

next_card()
window.mainloop()
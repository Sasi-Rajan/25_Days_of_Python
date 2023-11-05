from tkinter import *
import math
labeltext="✅"
#CONSTANTS VARIABLES
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "olivedrab"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25*60
SHORT_BREAK_SEC = 5*60
LONG_BREAK_SEC = 20*60
reps=0
timer=None

#WINDOW SETUP
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
#TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps=0


#TIMER MECHANISM
def start_timer():
    global reps
    if timer is not None:
        return
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_SEC)
        timer_label.config(text="Work", fg=GREEN)


#COUNTDOWN MECHANISM 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+=labeltext
        check_label.config(text=marks)

#UI SETUP
timer_label=Label(text="Timer",font=(FONT_NAME,28,"bold"),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0,column=1)

canvas=Canvas(window,width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_photo)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas.grid(row=1,column=1)


start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)


reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)


check_label=Label(bg=YELLOW,fg=GREEN)
check_label.grid(row=3,column=1)




window.mainloop()
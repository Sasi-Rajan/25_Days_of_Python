import turtle
import pandas
image=r"blank_states_img.gif"


screen=turtle.Screen()
screen.title("US STATE GAMES")

screen.addshape(image)
turtle.shape(image)

guessed_state=[]


data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()

while len(guessed_state) < 50:
    guess=screen.textinput(title=f"{len(guessed_state)}/50 states",prompt="Guess state names").title()
    if guess == "Exit":
        missed_states=[]
        for state in all_states:
            if state not in guessed_state:
                missed_states.append(state)
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in all_states:  
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data=data[data.state==guess]
            t.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
            t.write(guess)
            guessed_state.append(guess)

screen.mainloop()
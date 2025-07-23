from turtle import Turtle , Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title= "Make your bet" , prompt= "Which turtle will win the race? Enter a color: ")
color = ["red","orange","yellow","green","blue","purple"]
y_pos = [-70,-40,-10,20,50,80]

all_turtles = []
for turtle_index in range (0,6):
    t = Turtle(shape="turtle")
    t.color(color[turtle_index])
    t.penup()
    t.goto(x= -230, y=y_pos[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True
while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
               print(f"You won! The {winning_color} turtle is the winner.")
            else:
               print(f"You lose!, the winner is {winning_color} turtle.")
        dist = random.randint(0,10)
        t.forward(dist)

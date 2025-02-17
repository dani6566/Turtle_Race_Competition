from turtle import Turtle,Screen
import random


screen = Screen()
screen.title("Turtle Race Bet")

screen.setup(width=500,height=500)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ("red","orange","green","yellow","blue","purple")
y_position = [-100,-60,-20,20,60,100]

def prepare_turtle():
    all_turtles = []
    for index_turtle in range(0,6):
        emmy_turtle = Turtle(shape="turtle")
        emmy_turtle.color(colors[index_turtle])
        emmy_turtle.penup()
        emmy_turtle.goto(x=-220,y=y_position[index_turtle])
        all_turtles.append(emmy_turtle)
    return all_turtles

all_turtles = prepare_turtle()
if user_bet:
    is_race_on = True

while is_race_on:
    for single_turtle in all_turtles:
        if single_turtle.xcor() > 220:
            winner_color = single_turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle")
                is_race_on = False
                # screen.clear()
            else:
                print(f"You Lost. The {winner_color} turtle is the winner")
                is_race_on = False
                # screen.clear()
        single_turtle.penup()
        rand_num = random.randint(0,10)
        single_turtle.forward(rand_num)

    

screen.exitonclick()
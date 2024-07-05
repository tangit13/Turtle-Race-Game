from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(500, 600)
no_of_turtle = int(screen.textinput("No of turtles(Max no. of turtles=9)","Please enter the no. of turtle you want to race:"))
user_bet =  screen.textinput("Please make your bet", "Which turtle will win the race? Enter a choice: " )
colors = ["red", "orange", "yellow", "green", "blue", "purple", "peru", "pink", "cyan"]
y_positions = [-100, -70, -40, -10, 20, 50, 80, 110, 140]
all_turtles = []

#Creating 6 turtles
for i in range(0, no_of_turtle):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else :
                print(f"You've lost! The {winning_color} turtle is the winner!")


        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
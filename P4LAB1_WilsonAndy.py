#Andy Wilson
#03/25/2024
#P4LAB1A
#Shape with turtle

import turtle
win = turtle.Screen()
t = turtle.Turtle()

#add some display options
t.pensize(4) #increase pensize (takes integer)
t.pencolor("purple") # set pencolor (takes string)
t.shape("turtle")
#Draw Square
for square in range(4):
    #Actions to happen
    t.forward(100)
    t.left(90)
#Draw triangle
for triangle in range(3):
    t.forward(100)
    t.left(120)

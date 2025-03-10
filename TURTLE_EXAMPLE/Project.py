"""
Use the turtle module to draw a simple house with the following components:

A square for the house body.
A triangle on top as the roof.
A rectangle for the door.
(Bonus) Add windows or extra decorations.

"""
import turtle

# Setup the turtle
t = turtle.Turtle()
t.speed(3)

# Function to draw a square
def draw_square(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.left(90)
    t.end_fill()

# Function to draw a triangle (roof)
def draw_triangle(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

# Function to draw a rectangle (door)
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Draw the house body
t.penup()
t.goto(-100, -100)  # Move to start position
t.pendown()
draw_square(200, "blue")

# Draw the roof
t.penup()
t.goto(-100, 100)  # Move to top left of house
t.pendown()
draw_triangle(200, "brown")

# Draw the door
t.penup()
t.goto(-30, -100)  # Move to door position
t.pendown()
draw_rectangle(60, 100, "red")

# Draw the sun
t.penup()
t.goto(150, 150)  # Move to top right corner
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)  # Sun shape
t.end_fill()

# Draw sun rays
for _ in range(8):
    t.penup()
    t.goto(150, 190)  # Move to sun center
    t.pendown()
    t.forward(60)
    t.backward(60)
    t.right(45)

# Finish
t.hideturtle()
turtle.done()

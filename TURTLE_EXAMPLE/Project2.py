import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(3)

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a circle
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw car body
t.penup()
t.goto(-100, -50)
t.pendown()
draw_rectangle(200, 50, "red")

# Draw car roof
t.penup()
t.goto(-50, 0)
t.pendown()
draw_rectangle(100, 40, "blue")

# Draw front wheel
t.penup()
t.goto(-70, -60)
t.pendown()
draw_circle(20, "black")

# Draw rear wheel
t.penup()
t.goto(70, -60)
t.pendown()
draw_circle(20, "black")

# Draw a window
t.penup()
t.goto(-40, 10)
t.pendown()
draw_rectangle(30, 20, "white")

# Finish
t.hideturtle()
turtle.done()

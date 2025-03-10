import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(3)

# Function to draw an oval
def draw_oval(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, 90)
    t.circle(radius // 2, 90)
    t.circle(radius, 90)
    t.circle(radius // 2, 90)
    t.end_fill()

# Draw Minion body (yellow oval)
t.penup()
t.goto(-50, -100)
t.pendown()
draw_oval(100, "yellow")

# Draw Minion overalls (blue rectangle)
t.penup()
t.goto(-50, -20)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(80)
t.right(90)
t.forward(100)
t.right(90)
t.forward(80)
t.right(90)
t.end_fill()

# Draw Minion goggles strap
t.penup()
t.goto(-70, 50)
t.pendown()
t.pensize(10)
t.forward(140)
t.pensize(1)

# Draw Minion eyes (big white goggles)
t.penup()
t.goto(-30, 60)
t.pendown()
draw_oval(30, "white")

t.penup()
t.goto(30, 60)
t.pendown()
draw_oval(30, "white")

# Draw Minion pupils
t.penup()
t.goto(-20, 70)
t.pendown()
draw_oval(10, "black")

t.penup()
t.goto(20, 70)
t.pendown()
draw_oval(10, "black")

# Draw Minion smile
t.penup()
t.goto(-20, 20)
t.pendown()
t.setheading(-60)
t.circle(20, 120)

# Draw Minion hands
t.penup()
t.goto(-50, -20)
t.pendown()
t.setheading(180)
t.forward(30)

t.penup()
t.goto(50, -20)
t.pendown()
t.setheading(0)
t.forward(30)

# Draw Minion legs
t.penup()
t.goto(-30, -100)
t.pendown()
t.setheading(-90)
t.forward(30)

t.penup()
t.goto(30, -100)
t.pendown()
t.setheading(-90)
t.forward(30)

# Finish
t.hideturtle()
turtle.done()

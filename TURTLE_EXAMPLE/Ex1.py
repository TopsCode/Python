import turtle

# turtle.speed(3)


def draw_square(side_length,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.end_fill()

def draw_roof(side_length,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

def draw_door(width,height,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        

    turtle.end_fill()


turtle.penup() 
turtle.goto(-100,-100)
turtle.pendown()
draw_square(200,"blue")

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
draw_roof(200,"brown")

turtle.penup()
turtle.goto(-30,-100)
turtle.pendown()
draw_door(60,100,"green")

turtle.done()
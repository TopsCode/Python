#Drawing a Star

import turtle

turtle.color("gold")
turtle.begin_fill()

for _ in range(5):
    turtle.forward(100)
    turtle.right(144)

turtle.end_fill()
turtle.done()
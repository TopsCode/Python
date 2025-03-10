import turtle

t = turtle.Turtle()

# Move to (100, 100) while drawing
t.goto(100, 100)

# Lift pen up (no drawing)
t.penup()
t.goto(-50, 50)  # Moves without drawing

# Put pen down (start drawing again)
t.pendown()
t.goto(-100, -100)  # Draws a line to (-100, -100)

turtle.done()

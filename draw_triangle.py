def draw_triangle(turtle, x, y, leg):

    turtle.penup()
    turtle.color("orange")
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.seth(270)
    for i in range(3):
        turtle.forward(leg)
        turtle.left(120)
    turtle.end_fill()


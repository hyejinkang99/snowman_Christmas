# 별그리기 함수
def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


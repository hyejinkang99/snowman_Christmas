# 원그리기
def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

import turtle
from draw_circle import draw_circle
from draw_rectangle import draw_rectangle
from draw_star import draw_star
from draw_trapezoid import draw_trapezoid
from draw_triangle import draw_triangle
from moving_object import moving_object
from uAd_draw_trapezoid import uAd_draw_trapezoid


t = turtle.Turtle()
turtle.Screen().bgcolor("lightblue")
#속도
t.speed(0)
#캔버스 크기
turtle.setup(1000,700)
#시작 위치
x = 0
y = -70
#밤
draw_circle(t,"steelblue",500,150,270)
draw_circle(t,"cornflowerblue",300,150,270)
draw_circle(t,"steelblue",100,150,270)
draw_circle(t,"cornflowerblue",-100,150,270)
draw_circle(t,"steelblue",-300,150,270)
draw_circle(t,"cornflowerblue",-500,150,270)

# 트리의 줄기
draw_rectangle(t, "saddlebrown", x - 20, y - 70, 40, 70)

width = 250
height = 30
for i in range(12):
    width = width - 20
    x = 0 - width / 2
    draw_trapezoid(t, "green", x, y, width, height)
    #draw_circle(t, "red", x + random.randint(0, width), y + random.randint(0, height), 10)
    y = y + height

#바구니
uAd_draw_trapezoid(t, "pink", 15, -130, 70, 85)

#트리별
draw_star(t, "gold", -50, 300, 100)
#별
draw_star(t, "yellow", -490, 340, 10)
draw_star(t, "yellow", -400, 250, 20)
draw_star(t, "yellow", -300, 300, 50)
draw_star(t, "yellow", -200, 300, 10)
draw_star(t, "yellow", -150, 200, 50)
draw_star(t, "yellow", 100, 270, 30)
draw_star(t, "yellow", 200, 340, 15)
draw_star(t, "yellow", 300, 250, 40)
draw_star(t, "yellow", 400, 300, 30)



#눈사람1
draw_circle(t,"white", -400, -180, 70)
draw_circle(t,"white", -400, -50, 40)
draw_circle(t,"black",-413,-10,3)
draw_circle(t,"black",-387,-10,3)


#눈사람2
draw_circle(t,"white", -250, -180, 50)
draw_circle(t,"white", -250, -90, 30)
draw_circle(t,"black",-260,-57,2)
draw_circle(t,"black",-240,-57,2)

#3단 눈사람
draw_circle(t,"white", 250, -180, 80)
draw_circle(t,"white", 240, -70, 65)
draw_circle(t,"white", 230, 40, 40)
draw_circle(t,"black",215,100,2)
draw_circle(t,"gray",220,4,7)
t.pensize(3)
t.pencolor("saddlebrown")
t.penup()
t.goto(220,10)
t.pendown()
t.left(140)
t.forward(140)
t.right(80)
t.color("darkolivegreen1")
t.begin_fill()
t.circle(14)
t.end_fill()

#눈사람 코
draw_triangle(t,-403,-12,15)
draw_triangle(t,-253,-60,10)

#트리 오너먼트
draw_circle(t,"salmon",50,10,12)
draw_circle(t,"cyan",0,-10,14)
draw_circle(t,"salmon",-60,-30,12)
draw_circle(t,"cyan",-120,-60,14)
draw_circle(t,"darkorange",0,80,10)
draw_circle(t,"darkolivegreen1",-50,60,14)
draw_circle(t,"darkorange",-85,40,10)
draw_circle(t,"tomato3",18,170,12)
draw_circle(t,"steelblue",-20,150,14)
draw_circle(t,"tomato3",-62,127,11)

draw_circle(t,"yellow",400,-50,13)
draw_circle(t,"blue",450,-70,12)
draw_circle(t,"red",380,-60,11)
draw_circle(t,"pink",360,-100,12)
draw_circle(t,"hotpink",340,-90,12)
draw_circle(t,"red",400,-130,12)

draw_circle(t,"darkolivegreen1",340,-170,12)
draw_circle(t,"tomato3",450,-200,12)
draw_circle(t,"salmon",300,-200,14)
draw_circle(t,"cyan",360,-200,12)

t.penup()
t.color("brown")
t.goto(-340, -300)
t.write("Merry Christmas:)", font=("궁서", 50, "bold"))
t.goto(-700, -720)


turtle.exitonclick()






































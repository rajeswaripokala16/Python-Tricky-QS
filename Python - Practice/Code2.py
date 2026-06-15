from turtle import *

bgcolor("black")
speed(0)
up()
goto(0, -40)
down()

for i in range(25):
    for j in range(15):
        color(j/15, i/25, 1)
        right(90)
        circle(170 - i * 3, 90)
        left(90)
        circle(170 - i * 3, 90)
        right(180)
        circle(45, 24)

hideturtle()
done()

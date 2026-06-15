from turtle import *
from colorsys import *
setposition(0, -40)
bgcolor('black')
tracer(10)
h = 0
for i in range(700):
    h += 0.008
    color(hsv_to_rgb(h, 1, 1,))
    lt(32)
    fd(280)
    circle(-30, -150)
    fd(280)
    hideturtle()
done()

import math
from turtle import *

screen = Screen()
screen.bgcolor("black")
tracer(0)          # draw instantly
hideturtle()
pensize(2)

def heart_variant(t, mode=1):
    # mode 1: normal curve
    if mode == 1:
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    # mode 2: trapezium‑like (flatter top, wider bottom)
    elif mode == 2:
        x = 16 * math.sin(t) ** 3
        y = 11 * math.cos(t) - 8 * math.cos(2 * t) - 1.5 * math.cos(3 * t)
    # mode 3: stretched vertical heart
    else:
        x = 16 * math.sin(t) ** 3
        y = 18 * math.cos(t) - 6 * math.cos(2 * t) - math.cos(3 * t)

    return x, y

def draw_heart(mode, color_line, color_fill):
    penup()
    color(color_line, color_fill)
    begin_fill()
    for i in range(1000):
        t = 2 * math.pi * i / 1000
        x, y = heart_variant(t, mode)
        goto(x * 10, y * 10)   # scale up
        pendown()
    end_fill()

# draw three hearts to compare
draw_heart(1, "red", "#300000")      # normal
draw_heart(2, "deeppink", "#301020") # trapezium‑style
draw_heart(3, "orange", "#302000")   # tall variant

update()
done()
s

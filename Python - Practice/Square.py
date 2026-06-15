from turtle import *
from colorsys import hsv_to_rgb

bgcolor("black")
tracer(20)           # Fast rendering

h = 0                # Initial hue
b = "black"

for i in range(800):
    h += 0.007
    color(hsv_to_rgb(h, 1, 1), b)   # Change pen color gradually
    goto(0, 0)                      # Move to center
    begin_fill()
    fd(270)                         # Move forward 270 pixels
    rt(2)                           # Rotate right by 2 degrees
    circle(150, -90)                # Draw arc of circle
    end_fill()
    rt(90)                          # Rotate right by 90 degrees
    end_fill()
    hideturtle()

done()

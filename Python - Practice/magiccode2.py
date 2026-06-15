from turtle import *

tracer(10)
bgcolor("black")
col = ("magenta", "gold", "green")

for i in range(270):
    pencolor(col[i % 3])
    forward(i * 2)
    right(121)

hideturtle()
done()

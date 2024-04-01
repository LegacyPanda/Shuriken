import turtle as t
import colorsys

t.bgcolor("black")
t.tracer(100)
t.pensize(2)
josh = 0

for i in range(10000000000):
    c = colorsys.hsv_to_rgb(josh, 0.8, 1)
    t.pencolor(c)
    josh += 0.006

    t.right(119)
    t.circle(-i * 0.3, 120)
    t.circle(i * 0.3, 120)
    t.circle(-i * 0.3, 90)
    t.circle(i * 0.3, 90)

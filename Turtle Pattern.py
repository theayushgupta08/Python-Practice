import turtle
t = turtle.Turtle()
t.speed(450)
turtle.bgcolor("white")
for i in range(100):
    t.color("purple")
    t.circle(i)
    t.right(4)
turtle.done()
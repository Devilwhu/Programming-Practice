from turtle import Turtle
p=Turtle()
p.speed(5)
p.pensize(3)
p.color('brown','yellow')
p.begin_fill()
p.hideturtle()
for i in range(5):
   p.forward(200)
   p.right(144)
p.end_fill()

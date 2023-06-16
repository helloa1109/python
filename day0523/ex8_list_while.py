import turtle
colors=["red","purple","pink","green","orange","gray"]
t=turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length=10

while length<500:
    t.forward(length)
    t.pencolor(colors[length%7])
    t.right(144)
    length+5

while length<500:
    t.forward(length)
    t.pencolor(colors[length%7])
    t.right(144)
    length+=5
t.exitonclick()
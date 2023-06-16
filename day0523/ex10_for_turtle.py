import turtle as t

t.color("pink")
t.begin_fill()
t.pencolor("blue")
t.width(5)
n =4
for x in range(n):
    t.fd(70)
    t.lt(360/n)
t.end_fill()
t.exitonclick()
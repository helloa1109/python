import turtle as t

colors = ["blue", "yellow", "red", "black", "orange", "gray"]

t.speed(0)

for _ in range(500):
    for count in range(6):
        t.begin_fill()
        t.color(colors[count])
        t.circle(100)
        t.left(360/6)
        t.end_fill()

t.exitonclick()

import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
turtle.speed(2)
turtle.color("black")
turtle.pensize(3)

# Draw the cat's head
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

# Draw the cat's ears
turtle.penup()
turtle.goto(-60, 0)
turtle.pendown()
turtle.setheading(60)
turtle.circle(40, 120)
turtle.setheading(-60)
turtle.circle(40, 120)

# Draw the cat's eyes
turtle.penup()
turtle.goto(-40, 20)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(40, 20)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# Draw the cat's nose
turtle.penup()
turtle.goto(0, -20)
turtle.pendown()
turtle.setheading(-90)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.forward(15)
turtle.circle(15, 180)
turtle.forward(15)
turtle.end_fill()

# Draw the cat's mouth
turtle.penup()
turtle.goto(-40, -60)
turtle.pendown()
turtle.setheading(-60)
turtle.circle(40, 120)

# Draw the cat's whiskers
turtle.penup()
turtle.goto(-60, -30)
turtle.pendown()
turtle.setheading(65)
turtle.forward(40)

turtle.penup()
turtle.goto(-60, -40)
turtle.pendown()
turtle.setheading(65)
turtle.forward(40)

turtle.penup()
turtle.goto(-60, -50)
turtle.pendown()
turtle.setheading(65)
turtle.forward(40)

turtle.penup()
turtle.goto(60, -30)
turtle.pendown()
turtle.setheading(115)
turtle.forward(40)

turtle.penup()
turtle.goto(60, -40)
turtle.pendown()
turtle.setheading(115)
turtle.forward(40)

turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
turtle.setheading(115)
turtle.forward(40)

# Hide the turtle
turtle.hideturtle()

# Exit on click
turtle.done()

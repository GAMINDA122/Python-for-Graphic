import turtle
turtle.bgcolor('black')

ga = turtle.Turtle()
ga .speed(220)

for i in range(180):
    ga .color('red')
    ga .forward(90)

    ga .forward(20)
    ga .left(60)
    ga .color('green')
    ga .forward(40)
    ga .right(30)

    ga .penup()
    ga .setposition(0,0)
    ga .pendown()

    ga .right(2)

turtle.done()
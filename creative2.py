import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in('red','magenta','grey','pink','cyan','green','yellow'):
        turtle.color(colours)
        turtle.circle(100)
        turtle.right(10)


turtle.hideturtle()
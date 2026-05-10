import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("#2c2c2c") 

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-100, 50)
t.pendown()

t.color("red")
t.begin_fill()

for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)

t.end_fill()


t.penup()
t.goto(-20, 25)
t.pendown()

t.color("white")
t.begin_fill()

t.goto(-20, -25)
t.goto(40, 0)
t.goto(-20, 25)

t.end_fill()

t.end_fill()

t.hideturtle()

pantalla.exitonclick()


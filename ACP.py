import turtle
turtle.Screen().bgcolor("yellow")
t=turtle.Turtle()
t.fillcolor("orange")
t.begin_fill()
for _ in range(3):
    t.forward(90)
    t.right(120)
t.end_fill()
t.penup()
t.right(90)
t.forward(100)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
t.forward(74)
t.right(90)
t.forward(37)
t.right(90)
t.forward(74)
t.right(90)
t.forward(37)
t.end_fill()
t.penup()
t.backward(100)
t.left(67)
t.pendown()
t.fillcolor("red")
t.begin_fill()
for _ in range(6):
    t.forward(80)
    t.left(60)
t.end_fill()
turtle.done()



    

    

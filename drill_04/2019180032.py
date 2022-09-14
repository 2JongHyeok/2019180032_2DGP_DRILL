import turtle

i = 0

while i<6:
    if(i%2 == 0):
        turtle.forward(500)
        turtle.left(90)
        turtle.penup()
        turtle.forward(100)
        turtle.left(90)
        turtle.pendown()
        i+=1
    elif i == 5:
        turtle.forward(500)
        break
    else:
        turtle.forward(500)
        turtle.right(90)
        turtle.penup()
        turtle.forward(100)
        turtle.right(90)
        turtle.pendown()
        i+=1

i = 0
turtle.left(90)
while i<6:
    if(i%2 == 0):
        turtle.forward(500)
        turtle.left(90)
        turtle.penup()
        turtle.forward(100)
        turtle.left(90)
        turtle.pendown()
        i+=1
    elif i == 5:
        turtle.forward(500)
        break
    else:
        turtle.forward(500)
        turtle.right(90)
        turtle.penup()
        turtle.forward(100)
        turtle.right(90)
        turtle.pendown()
        i+=1

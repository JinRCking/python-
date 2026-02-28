import turtle
h=100
turtle.hideturtle() #BLANK，隐藏画笔
turtle.color("red") #BLANK，设置画笔的颜色
turtle.pensize(2)
turtle.goto(0,0)
for i in range(1,4):
    for j in range (1,3):
        turtle.forward(50)
        turtle.left(90)#BLANK，设置画笔的方向
        turtle.forward(h)
        turtle.left(90)
    h=h/2
    turtle.up()
    turtle.goto (i*50,0)
    turtle.down ()
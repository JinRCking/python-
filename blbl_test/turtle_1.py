import turtle as t
t.setup(700,700,10,20)
t.hideturtle()
t.color((1,0,0),(0,1,0))
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()
t.showturtle()
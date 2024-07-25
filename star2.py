import turtle, random
a=turtle.Turtle()
a.color('yellow')
s=turtle.Screen()
a.speed(5000)
s.bgcolor('black')
s.setup(700, 500)
def star(q, w):
    d=q//2*360/q
    a.begin_fill()
    for i in range(q):
        a.forward(w)
        a.left(d)
    a.end_fill()
for i in range(50):
    q1=random.randint(-780, 780)
    w1=random.randint(-480, 480)
    a.up()
    a.setposition(q1, w1)
    a.down()
    q=random.choice([7, 9, 11, 13])
    w=random.randint(20, 101)
    star(q, w)
def move(q1, w1):
    a.up()
    a.setposition(q1, w1)
    a.down()
    q=random.choice([7, 9, 11, 13])
    w=random.randint(20, 51)
    star(q, w)
s.onclick(move)
s.listen()
s.mainloop()
from turtle import Turtle,mainloop

def tree(plist,l,a,f):
    if l>5:
        lst=[]
        for p in plist:
            p.forward(l)
            q=p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)

def maketree(x,y):
    p=Turtle()
    p.color('green')
    p.pensize(10)
    p.speed(1)
    p.getscreen().tracer(30,0)
    p.left(90)
    p.hideturtle()

    p.penup()
    p.goto(x,y)
    p.pendown()
    t=tree([p],100,65,0.6375)
    print(len(p.getscreen().turtles()))

def maind():
    maketree(-200,-200)
    maketree(0,0)
    maketree(200,-200)
maind()
    

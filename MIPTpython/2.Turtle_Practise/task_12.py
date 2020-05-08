"""Drawing smile"""


from turtle import *


def task_12():
    shape('turtle')
    penup()
    forward(100)
    pendown()
    begin_fill()
    color("yellow")
    left(90)
    circle(100)
    end_fill()
    penup()
    goto(-30,50)
    begin_fill()
    color("blue")
    circle(10)
    end_fill()
    goto(30,50)
    begin_fill()
    color("blue")
    circle(10)
    end_fill()
    color("black")
    goto(0,0)
    width(5)
    pendown()
    forward(25)
    penup()
    goto(40,-30)
    color("red")
    pendown()
    circle(50,-180)
    done()

    
if __name__ == '__main__':
    task_12()
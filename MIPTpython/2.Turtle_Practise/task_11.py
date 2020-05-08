"""Drawing semicirle or arc"""


from turtle import *


def task_11():
    shape('turtle')
    setheading(90)
    radius=30
    count=int(input("amount of loops:"))
    while count>0:
        circle(-radius,180)
        circle(-radius/5,180)
        count-=1
    done()

    
if __name__ == '__main__':
    task_11()
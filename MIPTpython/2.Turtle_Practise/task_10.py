"""Drawing butterfly"""


from turtle import *


def task_10():
    shape('turtle')
    setheading(90)
    radius=50
    wings=int(input("wings:"))
    while wings>0:
        circle(radius)
        circle(-radius)
        radius+=20
        wings-=1
    done()

    
if __name__ == '__main__':
    task_10()
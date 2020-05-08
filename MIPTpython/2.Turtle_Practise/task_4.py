"""draw squares"""


from turtle import *


def task_4():
    x=10
    for _ in range(10):
        pendown()
        for _ in range(4):
            forward(x)
            left(90)
        penup()
        right(90)
        forward(10)
        right(90)
        forward(10)
        right(180)
        x+=20
    done()
        
    
if __name__ == '__main__':
    task_4()
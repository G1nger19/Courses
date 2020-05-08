"""Drawing square-spiral"""


from turtle import *


def task_7():
    shape('turtle')
    x=10
    for _ in range(20):
        forward(x)
        x+=10
        left(90)
    done()
    
if __name__ == '__main__':
    task_7()
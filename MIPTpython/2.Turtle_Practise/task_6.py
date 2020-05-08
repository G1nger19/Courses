"""Drawing spiral"""


from turtle import *
from math import pi, sin, cos



def task_6_1():
    shape('turtle')
    for i in range(200):
        t = i / 10 * pi
        dx = t * cos(t)
        dy = t * sin(t)
        goto(dx, dy)
    done()
def task_6_2():
    for i in range(1000):
        forward(i*0.1)
        left(10)
    
if __name__ == '__main__':
    task_6_2()
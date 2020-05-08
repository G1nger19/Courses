"""Drawing flower"""


from turtle import *


def task_9():
    shape('turtle')
    radius=50
    count=3
    angle_to_turn=360/count
    while count>0:
        circle(radius)
        circle(-radius)
        left(angle_to_turn)
        count-=1
    done()
    
if __name__ == '__main__':
    task_9()
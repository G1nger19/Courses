"""Drawing stars"""


from turtle import *


def task_13():
    peaks=int(input("star peaks:"))
    angle_to_turn=180/peaks_1
    penup()
    goto(10,0)
    pendown()
    setheading(180)
    while peaks>0:
        forward(200)
        left(180-angle_to_turn)
        peaks-=1
    done()

    
if __name__ == '__main__':
    task_13()
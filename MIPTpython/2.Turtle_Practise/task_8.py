"""Drawing n-true figuries"""


from turtle import *
import math

def task_8():
    shape('turtle')
    radius=10
    for number in range(3,11):
        penup()
        left((180-360/number)/2)
        pendown()
        for _ in range(number):
            left(360/number)
            forward(math.sin(math.pi/number)*2*radius)
        right((180-360/number)/2)
        penup()
        forward(10)
        radius+=10
    done()
    
if __name__ == '__main__':
    task_8()
"""draw lines and turtle's copies"""


from turtle import *


def task_5():
    n=int(input("Amount of lines:"))
    radius=float(input("Radius:"))
    shape('turtle')
    setheading(360/n)
    for _ in range(n):
        forward(radius)
        stamp()
        backward(radius)
        right(360/n)
    done()
        
    
if __name__ == '__main__':
    task_5()
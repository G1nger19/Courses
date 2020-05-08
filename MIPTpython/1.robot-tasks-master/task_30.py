#!/usr/bin/python3

from pyrob.api import *

def draw(length):
    i=0
    while i<length-1:
        if i>0:
            fill_cell()
            move_up()
        else:
            move_up()
        i+=1
    i=0
    while i<length-1:
        if i>0:
            fill_cell()
            move_right()
        else:
            move_right()
        i+=1
    i=0
    while i<length-1:
        if i>0:
            fill_cell()
            move_down()
        else:
            move_down()
        i+=1
    i=0
    while i<length-1:
        if i>0:
            fill_cell()
            move_left()
        else:
            move_left()
        i+=1
    i=0


@task(delay=0.10)
def task_9_3():
    count=1
    while not wall_is_beneath():
        move_down()
        count+=1
    while count>1:
        draw(count)
        move_right()
        move_up()
        count-=2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()

    pass


if __name__ == '__main__':
    run_tasks()

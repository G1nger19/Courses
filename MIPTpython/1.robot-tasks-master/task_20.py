#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(6):
        count=0
        while not wall_is_on_the_right() and count!=27:
            move_right()
            if not cell_is_filled():
                fill_cell()
                count+=1
        count=0
        move_down()
        while not wall_is_on_the_left() and count!=27:
            if not cell_is_filled():
                fill_cell()
                count+=1
            move_left()
        move_down()
        count=0
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()

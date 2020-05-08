#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    count=1
    move_right()
    while not wall_is_on_the_right():
        if not wall_is_above():
            count1=0
            while not wall_is_above():
                move_up()
                if not cell_is_filled():
                    fill_cell()
                count1+=1
            fill_cell()
            move_down(count1)
        move_right()
        count+=1
    if not wall_is_above():
        count1=0
        while not wall_is_above():
            move_up()
            if not cell_is_filled():
                fill_cell()
            count1+=1
        fill_cell()
        move_down(count1)
    move_left(count)
    pass


if __name__ == '__main__':
    run_tasks()

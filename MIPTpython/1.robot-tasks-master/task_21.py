#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    count=1
    while count!=14:
        count_2=count 
        while count_2!=0:
            if not cell_is_filled():
                fill_cell()
            move_right()
            count_2-=1
        move_down()
        move_left(count)
        count+=1
    pass


if __name__ == '__main__':
    run_tasks()

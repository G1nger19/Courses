#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def fill(a):    
        while a:
            move_right()
            fill_cell()
            move_down()
            fill_cell()
            move_down()
            fill_cell()
            move_up()
            move_right()
            fill_cell()
            move_left(2)
            fill_cell()
            move_up()
            if not a is 1:
                move_right(4)
            a-=1
    for row in range(4):
        fill(10)
        move_left(36)
        move_down(4)
    fill(10)
    move_left(36)
        
    pass


if __name__ == '__main__':
    run_tasks()

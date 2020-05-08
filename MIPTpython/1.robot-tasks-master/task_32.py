#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    count=0
    while not wall_is_on_the_right():
        if cell_is_filled():
            count+=1
        if wall_is_above():
            fill_cell()
        else:
            move_up()
            while not wall_is_above():
                if cell_is_filled():
                    count+=1
                else:
                    fill_cell()
                move_up()
            if cell_is_filled():
                count+=1
            else:
                fill_cell()
            while not wall_is_beneath():
                move_down()
        move_right()
    mov('ax',count)
    pass


if __name__ == '__main__':
    run_tasks()

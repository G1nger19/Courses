#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not wall_is_beneath():    
        while not wall_is_on_the_right():
            if not cell_is_filled():
                fill_cell()
            move_right()
        if not cell_is_filled():
            fill_cell()
        move_down()
        while not wall_is_on_the_left():
            if not cell_is_filled():
                fill_cell()
            move_left()
        if not cell_is_filled():
            fill_cell()
        if not wall_is_beneath():
            move_down()
    if wall_is_on_the_right():
        while not wall_is_on_the_left():
            if not cell_is_filled():
                fill_cell()
            move_left()
        if not cell_is_filled():
            fill_cell()
    else:
        while not wall_is_on_the_right():
            if not cell_is_filled():
                fill_cell()
            move_right()
        if not cell_is_filled():
            fill_cell()
        while not wall_is_on_the_left():
            move_left()
    
    pass


if __name__ == '__main__':
    run_tasks()

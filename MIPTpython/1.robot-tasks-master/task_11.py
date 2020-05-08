#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    if wall_is_above() and wall_is_beneath():
        fill_cell()
    while not wall_is_on_the_right():    #пока стены нет, идём вправо  
        if wall_is_above() and wall_is_beneath():
            fill_cell()
            move_right()
        else:
            move_right()
    if wall_is_above() and wall_is_beneath():
        fill_cell()
    pass


if __name__ == '__main__':
    run_tasks()

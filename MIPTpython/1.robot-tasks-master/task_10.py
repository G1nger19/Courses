#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    if not wall_is_beneath() and not wall_is_above():
        move_right()
    else:
        fill_cell()
        move_right()
    while not wall_is_on_the_right():    #пока стены, есть идём вправо  
        if not wall_is_beneath() and not wall_is_above():
            move_right()
        else:
            fill_cell()
            move_right()
    if not wall_is_beneath() and not wall_is_above():
        pass
    else:
        fill_cell()


if __name__ == '__main__':
    run_tasks()

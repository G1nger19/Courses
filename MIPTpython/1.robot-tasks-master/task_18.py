#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    #searching_exit
    while wall_is_above() and wall_is_beneath():
        if not wall_is_on_the_left():
            move_left()
        else:
            while wall_is_above() and wall_is_beneath():
                move_right()       
    #exit=up
    if not wall_is_above():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
    #exit=down
    else:
        move_down()
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_above():
            move_up()
    
    
    pass


if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    #left
    if wall_is_on_the_left():
        #up
        if wall_is_above():
            while not wall_is_on_the_right():
                move_right()
            while not wall_is_beneath():
                move_down()
        #down
        else:
            while not wall_is_on_the_right():
                move_right()
            while not wall_is_above():
                move_up()
    #right
    else:
        #up
        if wall_is_above():    
            while not wall_is_on_the_left():
                move_left()
            while not wall_is_beneath():
                move_down()
        #down
        else:
            while not wall_is_on_the_left():
                move_left()
            while not wall_is_above():
                move_up()
    pass


if __name__ == '__main__':
    run_tasks()

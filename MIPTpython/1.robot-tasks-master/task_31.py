#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_30():
    while True:
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()
        else:
            while wall_is_beneath() and not wall_is_on_the_right():
                move_right()
            if wall_is_beneath():
                while wall_is_beneath() and not wall_is_on_the_left():
                    move_left()
            if wall_is_beneath():
                break
    pass


if __name__ == '__main__':
    run_tasks()

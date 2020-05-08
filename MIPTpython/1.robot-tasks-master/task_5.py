#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():      
    while wall_is_beneath():    # пока стена снизу, двигаемся вправо   
        move_right()
    pass


if __name__ == '__main__':
    run_tasks()

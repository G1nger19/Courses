#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while wall_is_beneath() or wall_is_above():    #пока стены есть, идём вправо  
        move_right()


if __name__ == '__main__':
    run_tasks()

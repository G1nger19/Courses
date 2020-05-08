#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    count=0
    while count !=5:
        move_right()
        if cell_is_filled()==True:
            count+=1
    pass


if __name__ == '__main__':
    run_tasks()

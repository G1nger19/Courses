#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    count=0
    while True:
        if not wall_is_on_the_right():
            fill_cell()
            for c in range(count):
                if not wall_is_on_the_right():
                    move_right()
                else:
                    break
            count+=1
        else:
            break
            
    pass


if __name__ == '__main__':
    run_tasks()

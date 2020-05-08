#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():     
    for i in range(3):    #двигаемся лесенкой и закрашиваем клетку, когда будем на ней      
        move_right()
        move_down()
        if i==1:
            fill_cell()
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()

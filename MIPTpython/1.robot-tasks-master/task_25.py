#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    def fill(a):    
        while a:
            move_right()
            move_down()
            fill_cell()
            move_down()
            fill_cell()
            move_down()
            fill_cell()
            move_up()   
            fill_cell() 
            move_left()
            fill_cell()
            move_right(2)
            fill_cell()
            move_left()
            move_up(2)
            move_left()
            move_down()
            if not a is 1:
                move_up()
                move_right(4)
            a-=1
    fill(5)
    pass


if __name__ == '__main__':
    run_tasks()

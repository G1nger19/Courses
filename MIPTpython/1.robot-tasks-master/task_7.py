#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():    #пока стены снизу нету, идём вниз    
         move_down()
    while wall_is_beneath():        #пока стена есть, идём вправо
        move_right()
    move_down()                     #обходим стену
    move_left()
    while wall_is_above() and not wall_is_on_the_left():    #пока стена сверху есть и слева нету, идём влево 
        move_left()
    pass


if __name__ == '__main__':
    run_tasks()

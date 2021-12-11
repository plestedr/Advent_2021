# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:16:02 2021

@author: Plested
"""

import numpy as np
import os

os.chdir(r'C:\Users\agar2\OneDrive\Documents\github\Advent_2021\Advent_21_2')

Input_File = 'input_2a.txt'
#Input_File = 'example_2a.txt'

depth_file = open(Input_File, 'rt')

command = depth_file.readlines()

aim = 0
depth = 0
pos  = 0

for i in range(len(command)):
    current_command = command[i].split(' ')
    
    if current_command[0] == "forward":
        pos = pos + int(current_command[1])
        depth = depth + aim * int(current_command[1])
        
    elif current_command[0] == 'up':
        aim = aim - int(current_command[1])
   
    elif current_command[0] == 'down':
        aim = aim + int(current_command[1])
        
    else:
        print('Unrecognized')
        break

print(f'{depth * pos}')

depth_file.close()

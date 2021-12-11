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

depth = 0
pos  = 0

for i in range(len(command)):
    current_command = command[i].split(' ')
    
    if current_command[0] == "forward":
        pos = pos + int(current_command[1])
        
    elif current_command[0] == 'up':
        depth = depth - int(current_command[1])
   
    elif current_command[0] == 'down':
        depth = depth + int(current_command[1])
        
    else:
        print('Unrecognized')
        break

print(f'{depth * pos}')

# for i in range(3):
#     first_depth = first_depth + depth_list[i]

# print(f'First is {first_depth}')

# for j in range(1, len(depth_list)-2):
#     next_depth = 0
    
#     for i in range(3):
#         next_depth = next_depth + depth_list[j + i]
 
#     if next_depth > first_depth:
#         incr_count = incr_count + 1
        
#     print(f'next is {next_depth}, Increase is {incr_count}') 
#     first_depth = next_depth
    
depth_file.close()

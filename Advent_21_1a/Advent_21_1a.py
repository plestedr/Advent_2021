# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:16:02 2021

@author: Plested
"""

import numpy as np
import os

os.chdir(r'C:\Users\agar2\OneDrive\Documents\github\Advent_2021\Advent_21_1a')

Input_File = 'input_1a.txt'
#Input_File = 'example_1a.txt'

depth_file = open(Input_File, 'r')

first_depth = int(depth_file.readline())

incr_count = 0
print(f'First is {first_depth}')

for next_depth in depth_file:
    next_depth = int(next_depth) 
    
    if next_depth > first_depth:
        incr_count = incr_count + 1
        
    print(f'next is {next_depth}, Increase is {incr_count}') 
    first_depth = next_depth
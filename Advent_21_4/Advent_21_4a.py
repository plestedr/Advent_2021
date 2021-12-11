# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:00:00 2021
RR
@author: Plested
"""

import numpy as np
import os
# import keyboard

os.chdir(r'C:\Users\agar2\OneDrive\Documents\github\Advent_2021\Advent_21_4')
        
#Input_File = 'input_4a.txt'
Input_File = 'example_4a.txt'

bingo_file = open(Input_File, 'rt')

draw_list = list(map(int,bingo_file.readline().strip().split(",")))

status_int = []
sizeof_status = 0

for status_list in status_file:
    status_list = status_list.strip('\n')
    sizeof_status = max(len(status_list),sizeof_status)
    status_int.append(int(status_list, 2))
    print(f'{status_list}')
    
bingo_file.close()
    

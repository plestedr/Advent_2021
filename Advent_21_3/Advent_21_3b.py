# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:00:00 2021
RR
@author: Plested
"""

import numpy as np
import os
# import keyboard

os.chdir(r'C:\Users\agar2\OneDrive\Documents\github\Advent_2021\Advent_21_3')

def find_my_value(input_list, element_size, goal):
    for i in reversed(range(element_size)):
        if len(input_list) == 1:
            break
        bit_is_one = 0
        bit_is_zero = 0
        for j in range(len(input_list)):
            if input_list[j] & 1<<i:
                bit_is_one += 1 
            else:
                bit_is_zero += 1
        if bit_is_one > bit_is_zero:
            look_for_one = True
        elif bit_is_one < bit_is_zero:
            look_for_one = False
        elif (bit_is_one == bit_is_zero):
            look_for_one = True
        
        if 'l' in goal :
            look_for_one = not look_for_one
            
        for j in reversed(range(len(input_list))):
            if (look_for_one) and (not input_list[j] & 1<<i):
                input_list.pop(j)
            elif (not look_for_one) and (input_list[j] & 1<<i):
                input_list.pop(j)
    
    return int(input_list[0])
        
Input_File = 'input_3a.txt'
#Input_File = 'example_3a.txt'

status_file = open(Input_File, 'rt')

status_int = []
sizeof_status = 0

for status_list in status_file:
    status_list = status_list.strip('\n')
    sizeof_status = max(len(status_list),sizeof_status)
    status_int.append(int(status_list, 2))
    print(f'{status_list}')
    
status_file.close()
    
O2_int = find_my_value(status_int.copy(), sizeof_status, "m")
CO2_int = find_my_value(status_int.copy(), sizeof_status, "l")

print(f'Result is {O2_int * CO2_int}')

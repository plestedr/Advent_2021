# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:00:00 2021
RR
@author: Plested
"""

# import numpy as np
import os
# import keyboard

os.chdir(r'C:\Users\agar2\OneDrive\Documents\github\Advent_2021\Advent_21_3')

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
    
gamma = 0
epsilon = 0

for i in range(sizeof_status):
    bit_is_one = 0
    bit_is_zero = 0
    for j in range(len(status_int)):
        if status_int[j] & 1<<i:
            bit_is_one += 1 
        else:
            bit_is_zero += 1
    
    if bit_is_one > bit_is_zero:
        gamma = gamma + 2**i
    else:
        epsilon = epsilon + 2**i
#    junk = keyboard.read_key()
print(f'gamma and epsilon: {gamma, epsilon}')
print(f'gamma times epsilon: {gamma * epsilon}')



# aim = 0
# depth = 0
# pos  = 0

# for i in range(len(command)):
#     current_command = command[i].split(' ')
    
#     if current_command[0] == "forward":
#         pos = pos + int(current_command[1])
#         depth = depth + aim * int(current_command[1])
        
#     elif current_command[0] == 'up':
#         aim = aim - int(current_command[1])
   
#     elif current_command[0] == 'down':
#         aim = aim + int(current_command[1])
        
#     else:
#         print('Unrecognized')
#         break

# print(f'{depth * pos}')

status_file.close()

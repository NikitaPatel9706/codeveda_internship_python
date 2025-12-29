# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 22:03:34 2025

@author: NIKITA
"""

import random

print("number gueesing game")
rand_number=random.randint(1, 100)
max_attempt=7
print(f"you have only {max_attempt} to guess number \n")

for attemt in range(1,max_attempt+1):
    guess=int(input("enter your number:"))
    if guess <rand_number:
        print("too low\n")
    elif guess >rand_number:
        print("too high\n")
    else:
        print(f"the correct number is {rand_number}")
        print("you guess it!!")
        
        break
    
else:
    print("out of attempts")
    print(f"the correct answer is {rand_number}")
        
    
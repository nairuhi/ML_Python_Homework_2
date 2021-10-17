#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 18:20:05 2021

@author: nairuhi
"""

num = int(input())

print(num)

s = 0

while num > 0:
    digit = num % 10
    s += digit
    num = num // 10
    if num == 0:
        if s < 10:
            pass
        else:
            print(s)
            num = s
            s = 0
print(s)



    


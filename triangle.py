#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:21:50 2021

@author: nairuhi
"""

a = int(input())
b = int(input())
c = int(input())

small_side = min(a, b, c)
big_side = max(a, b, c)
middle_side = a + b + c - small_side - big_side


if small_side + middle_side == big_side:
    print("No Triangle")
elif small_side**2 + middle_side**2 == big_side**2:
    print("Right Triangle")
elif big_side**2 < small_side**2 + middle_side**2:
    print("Acute Triangle")
else:
    print("Obtuse Triangle")
    
    


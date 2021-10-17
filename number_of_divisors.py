#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:29:55 2021

@author: nairuhi
"""

x = int(input())

count = 0

for i in range (1, x+1):
    if x % i == 0:
        count += 1
print(count)
        
    
    
    
    
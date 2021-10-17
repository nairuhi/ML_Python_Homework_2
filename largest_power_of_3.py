#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:43:31 2021

@author: nairuhi
"""

N = int(input())

x = 0

while not 3**x > N:
    x += 1

print(3**(x-1))



    

    
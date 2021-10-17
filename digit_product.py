#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:34:02 2021

@author: nairuhi
"""

n = int(input())

product = 1

while n > 0:
    digit = n % 10
    if digit != 0:
        product *= digit
    n //= 10

print(product)


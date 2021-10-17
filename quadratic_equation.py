#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 22:06:30 2021

@author: nairuhi
"""

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print("Non-quadratic equation")
    if b == 0 and c == 0:
        print("Infinite solutions")
    elif b == 0:
        print("No solutions")
    else:
        print("One solution: ", -c/b)
else:
    print("Quadratic equation")
    D = b * b - 4 * a * c
    print("Discriminant: ", D)
    if D < 0:
        print("No Solutions")
    else:
        x1 = (-b - D**0.5)/2*a
        x2 = (-b + D**0.5)/2*a
        print("Two solutions: ", x1, x2)
    
    
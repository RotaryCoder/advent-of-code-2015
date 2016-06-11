# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:39:44 2015

@author: Dick84
"""
from itertools import combinations

import operator
import functools


t = list(range(1, 5))
for x in combinations(t, len(t)):
    print(x)
    
#stuff = [1, 2, 3]
for L in range(1, len(t)+1):
    for subset in combinations(t, L):
        x = functools.reduce(operator.mul, subset, 1)
        print(subset, x)
     
total = 0

#62,208,000 too high

maximum = 0
to_reach = 36000000
#i = int(to_reach / 2) - 1
i = 1

lowest = []

for k in range(1,50):
    factors = set()
    i = k
    total = 0
    while total < to_reach:
        
        i *= 2
            
            #    all_values = functools.reduce(operator.add, list(range(0,i)))
            #    if (all_values < to_reach):
            #        continue
            
        total = 0
        for j in range(i, 0, -1):
            if i % j == 0:
                total += j
                factors.add(j)
                total = total * 10
                #        print(j)
                if total > maximum:
                    maximum = total
#                        print(i, total)
                    #    if i > 10:
                    #        break
                    
                        
                        #    2685 = too low
    print(k, i, total, factors)
    
    
x = list(factors)
x.sort()
#print (x)

def merde(x):
    for i in range(1, len(x)):
        subset = x[0:i]
        total = functools.reduce(operator.mul, subset, 1) * 10
        print(subset, total, total > to_reach)
        if (total > to_reach):
            break
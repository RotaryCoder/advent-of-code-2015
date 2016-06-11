# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:41:29 2016

@author: Dick84
"""

from itertools import combinations
from operator import mul
from functools import reduce

with open('input.txt', 'r') as f:
    packages = f.read().splitlines()

packages = [int(x) for x in packages]
packages.reverse()

total_weight = sum(packages)
individual_weight = total_weight / 4
print(individual_weight)

min_x = 1
for i in range(1, len(packages)):
    if sum(packages[:i]) > individual_weight:
        min_x = i
        break
print(min_x)

found = False
for i in range(min_x, len(packages)):
    if found:
        break
    for p in combinations(packages, i):
        if sum(p) == individual_weight:
            found = True
            min_x = i
            print(i,p, sum(p))
            break
min_x = i - 1
        
min_qe = None
min_p = None
for p in combinations(packages, min_x):
    if sum(p) != individual_weight:
        continue
    qe = reduce(mul, p)
    if min_qe == None or min_qe > qe:
        print(p, qe)
        min_p = p
        min_qe = qe

print(min_p, min_qe)

#min_x = i

        
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:32:59 2016

@author: not Dick84
"""

import re

with open('input.txt', 'r') as f:
    input = f.read()

molecule = input.split('\n')[-1][::-1]
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input)}
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print(count)
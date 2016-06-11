# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:08:56 2016

@author: adrian17
"""

*replacements, mol = open("input.txt").read().splitlines()
replacements = [tuple(reversed(line.split())) 
                    for line in replacements if line != '']

starts = [mol]

for i in range(10000):
    print(starts)
    newstarts = set()
    for data in starts:
        for pattern, _, replacement in replacements:
            st = 0
            while True:
                loc = data.find(pattern, st)
                if loc == -1:
                    break
                new = data[:loc] + replacement + data[loc+len(pattern):]
                if new == "e":
                    raise Exception(str(i+1))
                newstarts.add(new)
                st = loc+1
    starts = sorted(newstarts, key=len)[:10]
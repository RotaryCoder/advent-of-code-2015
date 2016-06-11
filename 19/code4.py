# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:40:39 2016

@author: What-A-Baller
"""

from random import shuffle

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    
def tuples_from_lines(lines):
    t = []
    for l in lines:
        p = r'^(?P<from>.+) => (?P<to>.+)$'
        m = re.match(p, l)
        if not m:
            continue
        t.append((m.group('from'), m.group('to')))
    assert len(t) > 0, 'couldn''t extract tuples from lines'
    return t
    
def find_string(lines):
    for l in lines:
        if (len(l) > 20):
            return l
            
reps = tuples_from_lines(lines)
mol = find_string(lines)

target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print(part2)
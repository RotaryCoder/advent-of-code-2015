# -*- coding: utf-8 -*-

import re
from itertools import permutations
from math import factorial

with open('input.txt', 'r') as f:
    c = f.read()
desired = 150

p = r'(\d+)'
x = [int(i) for i in re.findall(p, c)]
possible = 0

#x = [5,5,10,15,20]
print(x)
#x.sort(reverse=True)
x.sort()
#desired = 25

min_l = 9999999

def get_min_l():
    return min_l

def func(d, l, prev):
#     min_l
    assert d > 0
    assert len(l) > 0
    total = 0
#    for i, value in enumerate(l):
    l2 = l[:]
    value = l2.pop()    
    if value == d:
        p = prev[:]
        p.append(value)
        total += 1
        global min_l
        global desired
        if len(p) <= min_l and sum(p) == desired:
            min_l = len(p)
            print(d, value, min_l, p)
    if len(l2) <= 0:
        return total
    if value < d:
        p = prev[:]
        p.append(value)
        total += func(d - value, l2, p)
    total += func(d, l2, prev)
    return total

print(func(desired, x, []))

# 4372

#func = sous liste qui exclue + sous-liste qui inclus

'''

def sub_list(toreach, l):
    assert toreach != 0
    total_v = 0
    if toreach < 0:
        return False, 0
    for i in range(len(l)):
        l2 = l[:]
        v = l2.pop(i)
        if v == toreach:
            total_v += 1
            continue
        else:
            e, v = sub_list(toreach - v, l2)
            if e == True:
                total_v +=v
    return v > 0, v

#print (sub_list(20, x))

#print(factorial(len(x)))
for i, y in enumerate(permutations(x), 1):
#    break
    if i % (4096 * 4096) == 0:
        print(i, possible)
        break
    total = 0
    for v in y:
        print(total)
        total += v
        print(total)
        if total == desired:
            possible += 1
            break
        if total > desired:            
            break

print(possible)

'''
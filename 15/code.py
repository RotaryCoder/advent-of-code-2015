# -*- coding: utf-8 -*-

from collections import namedtuple, defaultdict
import sys

with open('input.txt', 'r') as f:
    lines = f.readlines()

#Values = namedtuple('Values', ['c', 'd', 'f', 't', 'k'])
Values = namedtuple('Values', ['c', 'd', 'f', 't'])
properties = defaultdict(Values)

# Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
for line in lines:
    name, values = line.split(':')
    values = values.split(',')
    c = int(values[0].split()[1])
    d = int(values[1].split()[1])
    f = int(values[2].split()[1])
    t = int(values[3].split()[1])
#    k = int(values[4].split()[1])
    properties[name] = Values(c, d, f, t) #, k)
    print(name)

#print(properties)

def get_score(recipe):
    c = d = f = t = total = 0
    for n in recipe.keys():
        c += properties[n].c * recipe[n]
        d += properties[n].d * recipe[n]
        f += properties[n].f * recipe[n]
        t += properties[n].t * recipe[n]
    c = max(c, 0)
    d = max(d, 0)
    f = max(f, 0)
    t = max(t, 0)
    total = c * d * f * t
    return total

def get_ingredients_used(recipe):
    total = 0    
    for i in recipe.values():
        total += i
    return total

def find_least_enjoyable(recipe):
    min_score = 99999999999999
    min_ingredient = None
    r = recipe.copy()
    for n in r.keys():
        if r[n] == 0:
            continue
        r[n] -= 1
        score = get_score(r)
        if score < min_score:
            min_score = score
            min_ingredient = n
        r[n] += 1
    return min_ingredient

def find_most_enjoyable(recipe):
    max_score = -999999999
    max_ingredient = None
    r = recipe.copy()
    for n in r.keys():
        r[n] += 1
        score = get_score(r)
        if score > max_score:
            max_score = score
            max_ingredient = n
        r[n] -= 1
    assert max_ingredient != None, r
    return max_ingredient

r = defaultdict(int)
for name in properties.keys():
    r[name] = 100
while get_ingredients_used(r) > 100:
    n = find_least_enjoyable(r)
    r[n] -= 1

print(r)
print(get_score(r))
#

#
#r2 = defaultdict(int)
#for name in properties.keys():
#    r2[name] = 0
#while get_ingredients_used(r2) < 100:
#    n = find_most_enjoyable(r2)
#    r2[n] += 1
#    
#print(r2) 

#previous_score = get_score(recipe)
#for i in range(1):
#    for n in recipe.keys():
#        r = recip

#for i :


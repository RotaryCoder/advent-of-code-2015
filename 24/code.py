# -*- coding: utf-8 -*-

from itertools import permutations
from operator import mul
from functools import reduce

with open('input.txt', 'r') as f:
    packages = f.read().splitlines()

packages = [int(x) for x in packages]
packages.reverse()

total_weight = sum(p)
individual_weight = total_weight / 3
#print(indivdual_weight)

#print(t)
#for p in combinations(packages, 4, len(packages)):    
#    print(p)
#    group_1 = p[:index]
#        
#        
#        if (sum(group_1) < individual_weight):
#            continue
#        if (sum(group_1) > individual_weight):
#            break
#        print(group_1)
#        x += 1    
#    if x > 1:
#        break
#     

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        yield partial
#        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        yield from subset_sum(remaining, target, partial + [n]) 

x = 0
index = 3
d = {}

min_len = 99
min_QE = 0

def evaluate_set(i):
    global min_len
    global min_QE
    if len(i) > min_len:
        return
    if len(i) < min_len:
        min_len = len(i)
        min_QE = reduce(mul, i) + 1
        print('new min len: {}'.format(min_len))
    if i not in d:
        qe = reduce(mul, i)
        print(min_len, qe, i)
        d[i] = qe
        if qe < min_QE:
            min_QE = qe
            print('*** {}.'.format(qe))   

def evaluate_sets(i, j, k):
    evaluate_set(i)
    evaluate_set(j)
    evaluate_set(k)

for i in subset_sum(packages,indivdual_weight):
    i2 = frozenset(i)
    if i2 in d:
        continue
    else:
        sub = [x for x in packages if x not in i]
        for j in subset_sum(sub,indivdual_weight):
            j2 = frozenset(j)
            k2 = frozenset([x for x in sub if x not in j])
            evaluate_sets(i2, j2, k2)

# 163845007999 too high

# right 11846773891

#    
#    d[tuple(i)] = []
#    subset = [x for x in packages if x not in i]
#    for j in subset_sum(subset, individual_weight):
#        d[i].append(set(j))
#        print(i, j)

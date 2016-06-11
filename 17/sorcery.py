# -*- coding: utf-8 -*-

from numpy import vectorize

x = vectorize(int)(list(open('input.txt')))
c = 0
for i in range(1 << len(x)):
#    t = i
    s = 0
    for j in x:
        if i % 2 == 1:
            s += j
        i //= 2
    if s == 150:
        c += 1
print(c)
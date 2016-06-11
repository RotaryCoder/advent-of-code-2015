# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:58:06 2015

@author: Dick84
"""

with open('input.txt', 'r') as f:
    lines = f.readlines()

table = []
for line in lines:
    table.append(line.strip())
    
#table = [
#'.#.#.#',
#'...##.',
#'#....#',
#'..#...',
#'#.#..#',
#'####..']

def is_on(table, x, y):
    if table[x][y] == '#':
        return True
    return False
            
def calc_neighbours(table, x, y):
    total = 0
    max_x = len(table[0]) - 1
    max_y = len(table) - 1    
    assert x >= 0
    assert x <= max_x
    assert y >= 0
    assert y <= max_y
    for i in range(max(0, x - 1), min(x + 1, max_x) + 1):
        for j in range(max(0, y - 1), min(y + 1, max_y) + 1):
            if i == x and j == y:
                continue
            if is_on(table, i, j):
                total += 1
    return total

def on_or_off(table, x, y):
    # part 2
    max_x = len(table[0]) - 1
    max_y = len(table) - 1  
    if x == 0 or x == max_x:
        if y == 0 or y == max_y:
            return True
    # part 1
    total = calc_neighbours(table, x, y)
    on = is_on(table, x, y)
    if on and total >= 2 and total <= 3:
        return True
    if not on and total == 3:
        return True
    return False
                  
def iter_table(table):
    new_t = []
    for i, line in enumerate(table):
        new_t.append('')
        for j, c in enumerate(line):
            if on_or_off(table, i, j):
                new_t[i] += '#'
            else:
                new_t[i] += '.'
    return new_t
    
for i in range(100):
    table = iter_table(table)

grand_total = 0
for i, line in enumerate(table):
    for j, c in enumerate(table[i]):
        if is_on(table, i, j):
            grand_total += 1
print(grand_total)
        
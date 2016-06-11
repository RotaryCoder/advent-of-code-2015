# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:28:41 2016

@author: Dick84
"""

import re

string2 = 'HOHOHO'
lines2 = '''
e => H
e => O
H => HO
H => OH
O => HH
'''.splitlines()

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def find_string(lines):
    for l in lines:
        if (len(l) > 20):
            return l

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

evaluated = {}
def deconstruct(string, tuples, level = 0):
    global evaluated
    if string in evaluated:
        if evaluated[string] == 0:
            return False, 0
        else:
            return True, evaluated[string]
    if re.match(r'^e$', string):
        return True, level
    if re.search(r'e', string):
        return False, 0
    smallest_level = 0
    level += 1
    for t in tuples:
        p = t[1]        
        for m in re.finditer(p, string):
#            print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
#            string2 = string[:m.start()] + t[0] + string[m.end():]
            string2 = string.replace(p, t[0])
            print('({}) {} => {}'.format(level, string,string2))            
            b, l = deconstruct(string2, tuples, level)
            if (b):  
                evaluated[string] = l
                return b, l
                if smallest_level == 0 or l < smallest_level:
                    smallest_level = l
            else:
                evaluated[string2] = 0
    evaluated[string] = smallest_level
    if len(evaluated) % 10000 == 0:
        print('{} strings evaluated.'.format(len(evaluated)))
    if smallest_level != 0:
        return True, smallest_level
    return False, 0

string = find_string(lines)
t = tuples_from_lines(lines)
#print(t)

#print(string)
print(deconstruct(string, t))

# 205 too low
# 208 too high
# 215 too high


#print(evaluated)
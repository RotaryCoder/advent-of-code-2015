# -*- coding: utf-8 -*-

import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

begin_str = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'

#input
#lines = ['H => HO', 'H => OH', 'O => HH']
#lines = ['e => H', 'e => O','H => HO','H => OH','O => HH']
#begin_str = 'HOHOHO'

trans = []
d = {}
for line in lines:
#    print(line)
#    try:
    if line.strip() == '':
        break
    f, t = line.strip().split(' => ')
    trans.append((f, t))
    if t in d:
        raise
    d[t] = f
#    except:
#        break

outputs = set()

total = 0
def part_1():
    for i, c in enumerate(begin_str):
        left = begin_str[:i]
        right = begin_str[i:]
        #    print('{0}: {1}|{2}'.format(c, left, right, count=1))
        for f, t in trans:
            p = '^' + f
            r2, c = re.subn(p, t, right)
            print (r2, c)
            if c != 0:
                outputs.add(left + r2)

sorted_keys = sorted(d.keys(), key=lambda x : len(x), reverse=True)
#print(sorted_keys)

def part_2_2(substring):

    for i, c in enumerate(substring):
        left = substring[:i]
        right = substring[i:]
        assert len(left) + len(right) == len(substring)
        i1 = part_2_2(left)
        i2 = part_2_2(right)
        if i1 == None or i2 == None:
            return None
        return i1 + i2

levels = set()
def part_2(substring, level):
    print('doing {0}'.format(substring))
#    a = input()

    if substring.strip() == 'e':
        print('VICTOIRE {0}'.format(level))
        levels.add(level)
        return level
    possible = False        
    for f, t in trans:
        if re.match(t, substring):
            possible = True
            break
    if not possible:
        return None    
    for i, c in enumerate(substring):
        left = substring[:i]
        right = substring[i:]
        assert len(left) + len(right) == len(substring)
        for f, t in trans:
            if f == 'e' and len(left) > 0:
                continue
            if len(t) > len(right):
                continue
            if re.match(t, right):
#                print('found {0} in {1}'.format(t, right))   
                r2 = right.replace(t, f, 1)
#                if r2 == '':
#                    print('there')
#                r2 = re.sub(t, f, right, 1)
#                print('{0} is now {1}'.format(substring, left + r2))
#                print (left, r2)

                b = part_2(left + r2, level + 1)
    return None

xx = part_2(begin_str, 0)
#for x in xx:
#    if x != 9999999:
#        print(x)

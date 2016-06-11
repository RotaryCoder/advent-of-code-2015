# -*- coding: utf-8 -*-

import re

toto = 2
Sue = 'children: 3, cats: 7, samoyeds: 2, pomeranians: 3, \
akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, \
perfumes: 1'
r = None

t = r'''
import re
from collections import defaultdict

d = defaultdict(int)

print(globals()['toto'])

def main():
    t = 'asdfg 2 6  asdf 2'
    p = r'\d'
    d['yourmom'] = 100000
    return d

if __name__ == "__main__":
    globals()['r'] = main()
'''

exec(t)
print(r)

with open('input.txt', 'r') as f:
    lines = f.readlines()

def parse_line(line):
    # Sue 500: perfumes: 4, cars: 9, trees: 4
    p1 = r': '
    p2 = r', '
    p3 = r'(\w+): (\d)+'
    d = {}
    name, data = re.split(p1, line.strip(), 1)
    for x in re.split(p2, data):
        x = re.match(p3, x)
        assert x != None, 'Error parsing: ' + line
        d[x.group(1)] = int(x.group(2))
    return name, d

d = {}
for line in lines:
    name, values = parse_line(line)
    d[name] = values

print(list(d.items())[32])

def str_to_dict(s):
    p1 = r', '
    p2 = r': '
    d = {}
    s = s.strip()
    s = re.split(p1, s)
    try:
        for x in s:
            x = re.split(p2, x)
            d[x[0]] = int(x[1])
    except:
        raise ValueError(s)
    return d

def look_in_line(c):
    c = re.split(',', c.strip())
    found = False
    for x in c:
        if re.search(x, Sue):
            found = True
            continue
        else:
            found = False
            break
    return found

real_sue = str_to_dict(Sue)
def do_the_work(lines):
    for line in lines:
        n, c = re.split(': ', line.strip(), 1)
        d = str_to_dict(c)
    #    if (look_in_line(c)):
    #        print ('found ', n, c)
    #        break
        found = True
        for k in d.keys():
            if k == 'cats' or k == 'trees':
                if real_sue[k] >= d[k]:
                    found = False                
                    break
            elif k == 'pomeranians' or k == 'goldfish':
                if real_sue[k] <= d[k]:
                    found = False                
                    break        
            elif d[k] != real_sue[k]:
                found = False
                break
        if found:
            yield(n, d)

#    print(d)  

#    for element in line.split():
        
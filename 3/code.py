import sys
from sys import stdout
from collections import Counter

# from stdout import write

with open('input.txt', 'r') as f:
    file_data = f.read()
# print data

def navigate(data, begin, step):
    x = 0
    y = 0
    i = begin
    
    while i < len(data) :
        # get char and increment
        a_char = data[i]
        i += step

        #update coordinates    
        if a_char == '>':
            x += 1
        elif a_char == '<':
            x -= 1
        elif a_char == '^':
            y += 1
        elif a_char == 'v':
            y -= 1
        else:
            print a_char
        
        # yield tuple
        yield (x,y)

    
def create_map(data, begin, step):
    d = Counter({})
    for key in navigate(data, begin, step):
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d

map_santa = create_map(data=file_data, begin=0, step=1)
map_santa_with_robot = create_map(data=file_data, begin=0, step=2)
map_robot = create_map(data=file_data, begin=1, step=2)

print len(map_santa)
print len(map_santa_with_robot + map_robot)

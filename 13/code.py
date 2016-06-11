# -*- coding: utf-8 -*-

from sys import maxsize as BIG_BIG_NUMBER

with open('input.txt', 'r') as f:
    lines = f.readlines()

def words_to_int(words2, words3):
    if words2 == 'lose':
        sign = -1
    else:
        sign = 1
    return sign * int(words3)

def find_lowest_value(lines):
    min_value = BIG_BIG_NUMBER   
    for line in lines:
        words = line.split(" ")
        i = words_to_int(words[2], words[3])
        if i < min_value:
            min_value = i
    return min_value

def make_happy_dict(lines, min_value):
    arrangments = {}    
    for line in lines:
        words = line.rstrip('.\n').split(" ")
        if words[0] not in arrangments:
            arrangments[words[0]] = {}
        arrangments[words[0]][words[10]] = (
            words_to_int(words[2], words[3]) - min_value
            )
    return arrangments

min_value = find_lowest_value(lines)
happy_dict = make_happy_dict(lines, 0)

def calculate_sublist(happy_dict, sublist, before, after):
    best_i_can_do = 0
    best_next_person = None
    if len(sublist) == 1:
        person = sublist[0]
        i = 0
#        i += happy_dict[before][person]
        i += happy_dict[person][before]
        i += happy_dict[person][after]
        return i, person
    for person in sublist:
        try:        
            even_subber_list = sublist[:]
            even_subber_list.remove(person)
            happy, person = calculate_sublist(happy_dict, even_subber_list, person, after)
            even_subber_list = sublist[:]
            happy += happy_dict[before][person]
            happy += happy_dict[after][person]
            if happy > best_i_can_do:
                best_next_person = person
                best_i_can_do = happy
        except:
            print(person, before, after)
            raise
    return best_i_can_do, best_next_person

people= []
sublist = []
for i, p in enumerate(happy_dict.keys()):
    people.append(p)
sublist = people[:]
sublist.remove('Alice')
x, y = calculate_sublist(happy_dict, sublist, 'Alice', 'Alice')
print (x, y)

xx = happy_dict['Alice']['David']
print (x + xx)

# not 633
# not 797, too high

#print (lines[0].split(" "))
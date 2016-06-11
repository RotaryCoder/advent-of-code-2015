# -*- coding: utf-8 -*-

from sys import maxsize as BIG_BIG_NUMBER
from itertools import permutations
import numpy as np

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
            if 'me' not in arrangments:
                arrangments['me'] = {}
            arrangments[words[0]] = {}
            arrangments[words[0]]['me'] = 0
            arrangments['me'][words[0]] = 0
        arrangments[words[0]][words[10]] = (
            words_to_int(words[2], words[3]) - min_value
            )
    return arrangments

min_value = find_lowest_value(lines)
happy_dict = make_happy_dict(lines, 0)

def calculate_list(happy_dict, people):
    total_happy = 0
    for i, person in enumerate(people):
        i_before = (i - 1 + len(people)) % len(people)
        i_after  = (i + 1 + len(people)) % len(people)
        person_before = people[i_before]
        person_after  = people[i_after]
#        total_happy += happy_dict[person_before][person]
        total_happy += happy_dict[person][person_before]
        total_happy += happy_dict[person][person_after]
#        total_happy += happy_dict[person_after][person]
    return total_happy        

#def calculate_sublist(happy_dict, sublist, before, after):
#    best_i_can_do = 0
#    best_next_person = None
#    if len(sublist) == 1:
#        person = sublist[0]
#        i = 0
##        i += happy_dict[before][person]
#        i += happy_dict[person][before]
#        i += happy_dict[person][after]
#        return i, person
#    for person in sublist:
#        try:        
#            even_subber_list = sublist[:]
#            even_subber_list.remove(person)
#            happy, person = calculate_sublist(happy_dict, even_subber_list, person, after)
#            even_subber_list = sublist[:]
#            happy += happy_dict[before][person]
#            happy += happy_dict[after][person]
#            if happy > best_i_can_do:
#                best_next_person = person
#                best_i_can_do = happy
#        except:
#            print(person, before, after)
#            raise
#    return best_i_can_do, best_next_person

people= []
sublist = []
for i, p in enumerate(happy_dict.keys()):
    people.append(p)
#
#t = calculate_list(happy_dict, people)
#print(t)

max_happiness = 0
def calculate(happy_dict, people):
    l = []
    max_happiness = 0
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            l = []            
            for x in people[:i]:
                l.append(x)
            l.append(people[j])
            for x in people[i+1:j]:
                l.append(x)
            l.append(people[i])
            for x in people[j+1:]:
                l.append(x)
            if len(l)!=len(people):
                print(l)
                return
            happiness = calculate_list(happy_dict, l)
            print(l)
            if happiness > max_happiness:
                max_happiness = happiness
    return max_happiness
#            
#max_happiness = calculate(happy_dict, people)
#print (max_happiness)

def make_happy_matrix(happy_dict, people):
    matrix = []    
    for i, person_i in enumerate(people):
        row = []
        for j, person_j in enumerate(people):
            if i == j:
                row.append(np.NAN)
            else:
                row.append(
                happy_dict[person_i][person_j] +
                happy_dict[person_j][person_i]                
                )
        matrix.append(row)
    return np.matrix(matrix)

happy_matrix = make_happy_matrix(happy_dict, people)
happy_matrix -= np.nanmin(happy_matrix)
print(happy_matrix)

def make_happy_dict2(lines):
    arrangments = {}    
    for line in lines:
        words = line.rstrip('.\n').split(" ")
        x = words[0],words[10]
        arrangments[x] = (
            words_to_int(words[2], words[3])
            )
    return arrangments

happy2 = make_happy_dict2(lines)
def optimize(remainder, current, end):
    if len(remainder) == 0:
        return happy2[current, end]
    result = -99999999
    for next in remainder:
        r = remainder[:]
        r.remove(next)
        result = max(result, happy2[current, next] + optimize(r, next, end))
    return result

#start = people.pop()
#x= optimize(people, start, start)
#print(x)

max_happiness = 0
for x in permutations(people):
    happy = calculate_list(happy_dict, x)
    if happy > max_happiness:
        max_happiness = happy
        print(x)
print (max_happiness)

#sublist = people[:]
#sublist.remove('Alice')
#x, y = calculate_sublist(happy_dict, sublist, 'Alice', 'Alice')
#print (x, y)
#
#xx = happy_dict['Alice']['David']
#print (x + xx)

# not 633
# not 797, too high
# not 640, too low

#print (lines[0].split(" "))
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:19:55 2015

@author: Dick84
"""

import re
import json

def add_all_numbers(string):
    i = 0
    pattern= r"-*\d+"
    for item in re.findall(pattern, lines[0]):
        i += int (item)
    return i
    
def contains_red(string):
    pattern= r"red"
    if re.search(pattern, string):
        return True
    else:
        return False
    
def analyse_element(element):
    if type(element) is list:
        i = 0
        for sub_element in element:
            int_sum = analyse_element(sub_element)
            i += int_sum
        return i
    if type(element) is dict:
        if "red" in element.values():
            return 0
        i = 0
        for sub_element in element.items():
            int_sum = analyse_element(sub_element)
            i += int_sum
        return i
        
    if type(element) is tuple:
        int_sum = analyse_element(element[1])
        return int_sum
        
    try:
        i = int(element)
        return i
    except:
        return 0

# All numbers in file:
# Answer 1 = 191164


with open('input.txt', 'r') as f:       
    a = json.loads(f.read())

print(analyse_element(a))
#
#for i, x in enumerate(a):
#    print(str(x))
#    if i > 0:
#        break
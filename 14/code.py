# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:59:37 2015

@author: Dick84
"""
from collections import namedtuple, defaultdict
with open('input.txt', 'r') as f:
    lines = f.readlines()

Stamina = namedtuple('Stamina', ['speed', 'duration', 'rest', 'cycle'])
data = defaultdict(Stamina)

# Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
for line in lines:
    name,_,_,speed,_,_,duration,_,_,_,_,_,_,rest,_ = line.split()        
    speed = int(speed)    
    duration = int(duration)
    rest = int(rest)
    cycle = duration + rest
    data[name]=Stamina(speed,duration,rest,cycle)
#    print (data[name])

def calculate(deer, time):
    stamina = data[deer]
    cycles = time // stamina.cycle
    remainder = time % stamina.cycle
    duration = stamina.duration
    total = (cycles*duration + min(remainder, duration)) * stamina.speed        
    return total

def calculate_all(time):
    for deer in data.keys():        
        distance = calculate(deer, time)
        yield distance


def new_function(time):
    in_advance = defaultdict(int)
    for i in range(time):
        winning_deers = []
        best_dist = 1
        for deer in data.keys():
            x = calculate(deer, i)            
            if x > best_dist:
                best_dist = x
                winning_deers.clear()
            if x >= best_dist:
                winning_deers.append(deer)
        for deer in winning_deers:
            in_advance[deer] += 1
    return in_advance
            

print(max(calculate_all(2503)))
#    break

print(new_function(2503))
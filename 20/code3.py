# -*- coding: utf-8 -*-

from array import array

goal = int(36000000)
gifts_carried = 11

STOP_AFTER = 50
GIFTS_CARRIED = 11

goal = goal / 11
GIFTS_CARRIED = 1

def find_house(goal):
    houses = array('I', (0 for i in range(0, int(goal) + 1)))
    min_index = goal
    elf = 1
    while elf < min_index:
        elf_drops = elf * GIFTS_CARRIED
        for elf_stop in range (1, STOP_AFTER + 1):
            index = elf_stop * elf
            if index >= goal:
                break
            houses[index] +=  elf_drops
            if houses[index] > goal:
                if index < min_index:
                    min_index = index
        elf += 1
    return min_index

print(find_house(goal))

#RESULT: 884520

# too low  288288
# too high 1785126
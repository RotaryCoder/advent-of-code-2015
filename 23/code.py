# -*- coding: utf-8 -*-

import re
import logging
from collections import defaultdict

''' 
INSTRUCTIONS
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
'''

# Logger configuration:
logger = logging.getLogger('Day23')
#logger.setLevel(logging.WARN)
logger.format = '%(levelname)s:%(message)s'

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines();

index = 0    
registers = defaultdict(int)
registers['a'] = 1 # PART 2

def execute(instruction):
    parts = re.split('[ ,]', instruction.strip())
    parts = list(filter(None, parts))
    assert parts[0] in globals(), '{} not defined'.format(parts[0])
    assert len(parts) ==2 or len(parts) ==3, 'unable to parse'.format(
        instruction)
    if (len(parts) == 2):
        s = '{}(\'{}\')'.format(parts[0], parts[1])
    if (len(parts) == 3):
        s = '{}(\'{}\', \'{}\')'.format(
            parts[0], parts[1].strip(','), parts[2] )        
    logger.info(s)
    exec(s)

def inc(r):
    registers[r] += 1
    move_next()

def hlf(r):
    registers[r] //= 2
    move_next()

def tpl(r):
    registers[r] *= 3
    move_next()

def jio(x, y):
    global index
    if registers[x] ==1:
        index += int(y)
    else:
        move_next()

def jie(x, y):
    global index
    if registers[x] % 2 == 0:
        index += int(y)
    else:
        move_next()

def move_next():
    global index
    index += 1

def jmp(x):
    global index
    index += int(x)

while index < len(instructions):
    logger.debug('LINE({}) {}'.format(index, instructions[index]))
    execute(instructions[index])    

print(registers)
# -*- coding: utf-8 -*-

import logging

# Logger configuration:
logger = logging.getLogger('Day25')
logger.setLevel(logging.INFO)
logger.format = '%(levelname)s:%(message)s'

#DAY 25
FIRST_CODE = 20151125
MULT_VALUE = 252533
MODULO = 33554393

second_code = FIRST_CODE * MULT_VALUE % MODULO
#print (second_code)

# total = 2 (1,1)
# total = 3 (2,1), (1,2)
# total = 4 (3,1), (2,2), (1,3)

# Enter the code at row 2947, column 3029.
row = 2947
col = 3029

#row = 1
#col = 4

def find_code(desired_row, desired_col):
    assert desired_row > 0, 'code table starts at index 1,1'    
    assert desired_col > 0, 'code table starts at index 1,1'
    code = 20151125
    logger.info('finding the code at row {}, column {}'.format(
        desired_row, desired_col))
    if desired_col == 1 and desired_row == 1:
        return code
    for total in range(3, desired_row + desired_col + 1):
        logger.debug('total:{}'.format(total))
#        table_part.append([])
        for col in range(1, total):
            row = total - col
            code = code * MULT_VALUE % MODULO
#            if row <= 6 and col <= 6:
#                table_part[col-1].append(new_code)
            if (desired_row, desired_col) == (row, col):
                return code

# RIGHT ANSWER : 19980801
code = find_code(row, col)
print('{0} {1}'.format((row,col), code))

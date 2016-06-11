import sys
from sys import stdout
# from stdout import write


def HowMuchPaper(sides):
  min1 = min(sides)
  index = sides.index(min1)
  subvalues = sides[: index] + sides[index+1 :] 
  min2 = min(subvalues)
  # print subvalues
  # print sides
  area = (sides[0]*sides[1] * 2) \
    + (sides[0]*sides[2] * 2) \
    + (sides[1]*sides[2] * 2)
  total = area + min1 * min2
  # print str(sides) + " : " + str(total)
  return total
  
def HowMuchRibbon(sides):
  min1 = min(sides)
  index = sides.index(min1)
  subvalues = sides[: index] + sides[index+1 :] 
  min2 = min(subvalues)
  # print subvalues
  # print sides
  perimeter = min1 * 2 + min2 * 2
  total = perimeter + sides[0] * sides[1] * sides[2]
              # reduce(lambda x, y: x*y, sides)
  # print str(sides) + " : " + str(total)
  return total
  

HowMuchPaper([2, 3, 4])  
HowMuchPaper([1, 1, 10])

TotalPaper = 0
TotalRibbon = 0
with open('input.txt') as f:
  for line in f:
    sides = line.rstrip().split('x')
    sides = map(int, sides)
    TotalPaper += HowMuchPaper(sides)
    TotalRibbon += HowMuchRibbon(sides)
    
print "Paper:  " + str(TotalPaper)
print "Ribbon: " + str(TotalRibbon)

import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

prop = dict([])
for line in lines:
    pattern = r'[ ,]+'
    n, p = line.strip().split(':')
    p = re.split(pattern, p.strip())
    x = [int(j) for i,j in enumerate(p) if i %2 == 1]
    prop[n] = x
print(prop)

#t= [
#[3, 0, 0, -3, 2],
#[-3, 3, 0, 0, 9],
#[-1, 0, 4, 0, 1],
#[0, 0, -2, 2, 8],
#]

def get_score(recipe):
    c = d = f = t = total = 0
    for n in recipe.keys():
        c += prop[n][0] * recipe[n]
        d += prop[n][1] * recipe[n]
        f += prop[n][2] * recipe[n]
        t += prop[n][3] * recipe[n]
    c = max(c, 0)
    d = max(d, 0)
    f = max(f, 0)
    t = max(t, 0)
    total = c * d * f * t
    return total

def get_calories(recipe):
    total = 0
    for n in recipe.keys():
        total += prop[n][4] * recipe[n]
    return total

def make_recipe(*args):
    recipe = {}
    for i, ing in enumerate(prop.keys()):
        recipe[ing] = args[i]
    return recipe

print (make_recipe(25,24,23,22))
'''
'''
max_score = 0

for i in range(0,100):
    for j in range(0,100-i):
        for k in range(0,100-i-j):
            h = 100-i-j-k
            recipe = make_recipe(i,j,k,h)

            calories = get_calories(recipe)
            if (calories != 500):
                continue

            score = get_score(recipe)
#            score = 0 
#            a = t[0][0]*i+t[1][0]*j+t[2][0]*k+t[3][0]*h
#            b = t[0][1]*i+t[1][1]*j+t[2][1]*k+t[3][1]*h
#            c = t[0][2]*i+t[1][2]*j+t[2][2]*k+t[3][2]*h
#            d = t[0][3]*i+t[1][3]*j+t[2][3]*k+t[3][3]*h
#            e = t[0][4]*i+t[1][4]*j+t[2][4]*k+t[3][4]*h
#
#            #extra condition for part b
##            if(not(e == 500)):
##                continue
#            if (a <= 0 or b <= 0 or c <= 0 or d <= 0):
#                score = 0
#                continue
#            score = a*b*c*d
            if (score > max_score):
                max_score = score

print(max_score)
# 18965440 too high
'''
# '''
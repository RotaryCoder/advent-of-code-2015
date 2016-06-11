
def apply_on_range(map, coords, func):
    begin = coords[0]
    end = coords[1]
    for x in range(int(begin[0]), int(end[0]) + 1):
        for y in range(int(begin[1]), int(end[1]) + 1):
            func(map, x, y)

def toggle(map, x, y):
    map[x][y] = not map[x][y]
    
def turn_on(map, x, y):
    map[x][y] = True
    
def turn_off(map, x, y):
    map[x][y] = False

# PART DEUX ###########################################################
def toggle_2(map, x, y):
    map[x][y] += 2
    
def turn_on_2(map, x, y):
    map[x][y] += 1
    
def turn_off_2(map, x, y):
    assert map[x][y] >= 0, "value should never go below 0"
    if map[x][y] == 0:
        return
    map[x][y] -= 1
# END PART DEUX #######################################################
    
def part_coord_string(coord_string):
    words = coord_string.split(" ")
    begin_string = words[0]
    end_string = words[2]
    begin = with_comma_to_tuple(begin_string)
    end = with_comma_to_tuple(end_string)
    assert end[0] >= begin[0], "error parsing " + coord_string
    assert end[1] >= begin[1], "error parsing " + coord_string
    return begin, end
    
def with_comma_to_tuple(word):
    parts = word.split(",")
    v0 = int(parts[0])
    v1 = int(parts[1])
    return (v0, v1)

def apply_line(map, line):
    print(line)
    if (line.startswith("turn on ")):
        operation = turn_on
        coord_string = line[8:]
    elif (line.startswith("turn off ")):
        operation = turn_off
        coord_string = line[9:]
    elif (line.startswith("toggle ")):
        operation = toggle
        coord_string = line[7:]
    coords = part_coord_string(coord_string)
    # begin = coords[0]
    # end = coords[1]
    # print(str(coords) + " w:" + str(end[0] - begin[0]) + " h:" + str(end[1] - begin[1]))
    apply_on_range(map, coords, operation)
    
def apply_line_2(map, line):
    # print(line)
    if (line.startswith("turn on ")):
        operation = turn_on_2
        coord_string = line[8:]
    elif (line.startswith("turn off ")):
        operation = turn_off_2
        coord_string = line[9:]
    elif (line.startswith("toggle ")):
        operation = toggle_2
        coord_string = line[7:]
    coords = part_coord_string(coord_string)
    # begin = coords[0]
    # end = coords[1]
    # print(str(coords) + " w:" + str(end[0] - begin[0]) + " h:" + str(end[1] - begin[1]))
    apply_on_range(map, coords, operation)    



with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    
# PART 2
map_2 = [[0 for x in range(1000)] for x in range(1000)]     

for line in lines:
    apply_line_2(map_2, line)
    
count_2 = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        count_2 += int(map_2[i][j])
print(count_2)
# REPONSE: 14110788

# PART 1
# map = [[False for x in range(1000)] for x in range(1000)]  

# for line in lines:
    # apply_line(map, line)

# ESSAI #1: 377035 (FAUX)
# REPONSE: 377891
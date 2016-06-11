#filename = 'input.txt'
filename = 'test_input.txt'
with open(filename, 'r') as f:
    lines = f.read().splitlines()

def shortest_path(distances, cities_to_visit):
    assert len(cities_to_visit) >= 2, 'Not enough cities to continue'
    if len(cities_to_visit) == 2:
        d = distances[(cities_to_visit[0], cities_to_visit[1])]
        end1 = cities_to_visit[0]
        end2 = cities_to_visit[1]
        return d, end1, end2
    min_distance = -1
    for city in cities_to_visit:
        c = cities_to_visit[:]
        c.remove(city)
        (distance, opt1, opt2) = shortest_path(distances, c)
        d1 = distance + distances[(opt1, city)]
        d2 = distance + distances[(opt2, city)]
        assert d1 != d2, 'yish'
        assert d1 != min_distance, 'yish'
        assert d2 != min_distance, 'yish'
        if d1 < d2:
            if min_distance < 0 or d1 < min_distance:
                min_distance = d1
                end1 = city
                end2 = opt2
        else:
            if min_distance < 0 or d2 < min_distance:
                min_distance = d2
                end1 = city
                end2 = opt1
    return min_distance, end1, end2

def from_line_to_elements(line):
    elements = line.split(' ')
    source = elements[0]
    destination = elements[2]
    distance = int(elements[4])
    return source, destination, distance

distances = {}
a_map = {}
current_location = None
list_of_cities = []

for i, line in enumerate(lines):
    source, dest, dist = from_line_to_elements(line)
    distances[(source, dest)] = dist
    distances[(dest, source)] = dist
    if source not in list_of_cities:
        list_of_cities.append(source)
    elif dest not in list_of_cities:
        list_of_cities.append(dest)

print(shortest_path(distances, list_of_cities ))

assert False, "THIS CODE DOESNT HANDLE EQUALITIES"

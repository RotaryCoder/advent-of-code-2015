filename = 'input.txt'
#filename = 'test_input.txt'
with open(filename, 'r') as f:
    lines = f.read().splitlines()


def shortest_path(distances, starting_point, cities_to_visit):
    assert len(cities_to_visit) >= 2, 'Not enough cities to continue'
    if len(cities_to_visit) == 2:
        d1 = (distances[(starting_point, cities_to_visit[0])]
                + distances[(cities_to_visit[0], cities_to_visit[1])])
        d2 = (distances[(starting_point, cities_to_visit[1])]
                + distances[(cities_to_visit[1], cities_to_visit[0])])
        if d1 < d2:
            return d1
        else:
            return d2
    min_distance = -1
    for city in cities_to_visit:
        c = cities_to_visit[:]
        c.remove(city)
        distance = shortest_path(distances, city, c)
        distance += distances[(starting_point, city)]
        assert distance != min_distance, 'yish'
        if min_distance < 0 or distance < min_distance:
            min_distance = distance
    return min_distance

def find_shortest_path_and_city(distances, cities_to_visit):
    min_distance = -1
    min_city = ''
    for city in cities_to_visit:
        c = cities_to_visit[:]
        c.remove(city)        
        distance = shortest_path(distances, city, c)
        if min_distance < 0 or distance < min_distance:
            min_distance = distance
            min_city = city
    return min_distance, min_city

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


print(find_shortest_path_and_city(distances, list_of_cities ))

assert False, "THIS CODE DOESNT HANDLE EQUALITIES"

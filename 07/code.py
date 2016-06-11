import re

filename = 'input.txt'
# filename = 'test_input.txt'
with open(filename, 'r') as f:
    lines = f.read().splitlines()

mapped = {'b':19138, 'c':0}

def contains_operator(line):
    pattern = r"(AND)|(SHIFT)|(OR)|(NOT)"
    if re.search(pattern, line):
        return True
    else:
        return False

def split_parts(line):
    parts = line.split(" -> ")
    left = parts[0]
    right = parts[1]
    return left, right

def is_evaluable(part):
    try:
        value = int(part)
        return True
    except:
        return False

def find_equivalent_in_input(word):
    for line in lines:
        left, right = split_parts(line)
        if word == right:
            return left

def recursive_evaluate(left):
    parts = left.split(" ")
    if len(parts) == 1:
        identifier = parts[0]
        if is_evaluable(identifier):
            return int(identifier)
        else:
            if identifier in mapped:
                print("known " + identifier + "="+ str(mapped[identifier]))
                return mapped[identifier]
            equivalent = find_equivalent_in_input(identifier)
            # print(left + "==" + equivalent)
            assert equivalent is not None, "error evaluating part[0]" + left
            value = recursive_evaluate(equivalent)
            mapped[identifier] = value
            return int(value)

    if re.search("NOT", left):
        assert len(parts) == 2, "not should have 2 lines" + left
        return 0xFFFF ^ recursive_evaluate(parts[1])

    if re.search("RSHIFT", left):
        assert len(parts) == 3, "rshift should have 3 parts" + left
        value = recursive_evaluate(parts[0])
        shift = int(parts[2])
        # assert shift < 8, left + " shift:" + str(shift)
        return (value >> shift) & 0xFFFF

    if re.search("LSHIFT", left):
        assert len(parts) == 3, "lshift should have 3 parts" + left
        value = recursive_evaluate(parts[0])
        shift = int(parts[2])
        # assert shift < 8, left + " shift:" + str(shift)
        return (value << shift) & 0xFFFF

    if re.search("AND", left):
        assert len(parts) == 3, "and should have 3 parts" + left
        v0 = recursive_evaluate(parts[0])
        v1 = recursive_evaluate(parts[2])
        return v0 & v1

    if re.search("OR", left):
        assert len(parts) == 3, "and should have 3 parts" + left
        v0 = recursive_evaluate(parts[0])
        v1 = recursive_evaluate(parts[2])
        return v0 | v1        

    raise ValueError('What is this: ' + left)

# # # # # # # # # # # # # # # # # # # # # # # TEST 
# # 123 -> x
# # 456 -> y
# # x AND y -> d
# # x OR y -> e
# # x LSHIFT 2 -> f
# # y RSHIFT 2 -> g
# # NOT x -> h
# # NOT y -> i
# print recursive_evaluate("d") # d: 72
# print recursive_evaluate("e") # e: 507
# print recursive_evaluate("f") # f: 492
# print recursive_evaluate("g") # g: 114
# print recursive_evaluate("h") # h: 65412
# print recursive_evaluate("i") # i: 65079
# print recursive_evaluate("x") # x: 123
# print recursive_evaluate("y") # y: 456
# # # # # # # # # # # # # # # # # # # # # # # TEST 

print recursive_evaluate("a") # y: 456

for line in lines:
    if not contains_operator(line):
        print(line)

# print(recursive_evaluate("gp"))
    
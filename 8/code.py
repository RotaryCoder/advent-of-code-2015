import ast

filename = 'input.txt'
# filename = 'test_input.txt'
with open(filename, 'r') as f:
    lines = f.read().splitlines()
    
    # # # # # # # # # # # # # # TEST
val_map = { "":(2,0), 
            "abc":(5,3), 
            "aaa\"aaa":(10,7), 
            "\x27":(6,1) }
            
enc_map = { "":(6), 
            "abc":(9), 
            "aaa\"aaa":(16), 
            "\x27":(11) }
 # # # # # # # # # # # # # # TEST
map = {}    
count_1 = 0
count_2 = 0
    
for line in lines:
    map[line] = (len(line), len(ast.literal_eval(line)))
    repres = repr(line)
    size_2 = line.count('"') + line.count('\\') + len(line) + 2
    # print(line + " "*(12-len(line)) + str(size2))
    count_1 += (len(line) - len(ast.literal_eval(line)))
    count_2 += size_2 - len(line) 
    
print count_1, count_2
import time

input = '1113222113'

MAX_ITER = 5
iter = 0

def make_longer_string(input):
    int(input)
    prev_c = None
    consecutive = 0
    result = ''
    for i,c in enumerate(input):
#        print(i, c)
        if prev_c != c:
            if prev_c != None:
                result += str(consecutive) + prev_c
            consecutive = 1
            prev_c = c
            continue
        else:
            consecutive += 1
    result += str(consecutive) + c
    return result
            

def iterate_many_times(value, times):
    growth = 1.0
    prev_len = len(value)
    for i in range(times):
        start_time = time.time()
        value = make_longer_string(value)
        elapsed_time = time.time() - start_time
        growth = len(value)/prev_len
        prev_len=len(value)
#       print(growth, elapsed_time)
    return len(value), growth

Lambda = 1.303577269034
#_, _, growth40 = iterate_many_times(input, 40)
#_, _, growth41 = iterate_many_times(input, 41)
#_, _, growth42 = iterate_many_times(input, 42)

#print (growth40, growth41, growth42)
#iterate_many_times('1', 10)
x= iterate_many_times(input, 40)
print(x)
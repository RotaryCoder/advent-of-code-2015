
import itertools

input = 36000000

flatten_iter = itertools.chain.from_iterable

def get_factors(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))

for n in range(6, 6000000, 6):
    print (n, sum(get_factors(n)))
    if(10 * sum(get_factors(n))) >= input:
        print(n)
        break
import math
import timeit

setup = """
from __main__ import integrate
import math
"""

def integrate(fn, a, b, countOfSteps=10000):
    result = 0
    h = 1 / countOfSteps
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return result
        
print( integrate(math.cos, 0, 1) )

if __name__ == '__main__':
    print(timeit.timeit(stmt='integrate(math.cos, 0, 1)', setup=setup, number=10000)) # my result 12.5 sec

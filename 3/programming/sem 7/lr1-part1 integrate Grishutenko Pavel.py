import math


def integrate(fn, a, b, countOfSteps=10000):
    result = 0
    h = 1 / countOfSteps
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return result
        
        
print( integrate(math.cos, 0, 1) )
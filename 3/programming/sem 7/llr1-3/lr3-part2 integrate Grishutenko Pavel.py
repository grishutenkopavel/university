import cython
import math
import timeit
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from cint import c_integrate

timeitSetup = """

import math
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from __main__ import integrate
from __main__ import integrate_async
from __main__ import c_integrate_async
from cint import c_integrate
"""


def integrate(fn, a, b, countOfSteps=10**6):

    result= 0
    h = 1 / countOfSteps
    rightBorder = b - h
    while a <= rightBorder:
        result += (fn(a) + fn(a + h)) / 2
        a += h
    return result * h



def integrate_cython(fn: cython.pointer, a: cython.float , b: cython.float , countOfSteps: cython.float =10**6) -> cython.float:

    result: cython.float = 0
    h: cython.float = 1 / countOfSteps
    rightBorder: cython.float = b - h
    while a <= rightBorder:
        result += (fn(a) + fn(a + h)) / 2
        a += h
    return result * h

def integrate_async(f, a, b, n_jobs=8, n_iter=10**6):

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        spawn = partial(executor.submit, integrate_cython, f, countOfSteps=n_iter // n_jobs)
        step = (b - a) / n_jobs
        fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        return sum(f.result() for f in as_completed(fs))


def c_integrate_async(a, b, n_jobs=8, n_iter=10**6):

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        spawn = partial(executor.submit, c_integrate(0, 1), countOfSteps=n_iter // n_jobs)
        step = (b - a) / n_jobs
        fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        return sum(res.result() for res in as_completed(fs))

if __name__ == '__main__':
    
    # Multithreading
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=2)', setup=timeitSetup, number=100)) # ~ 5 sec
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=4)', setup=timeitSetup, number=100)) # ~ 2.5 sec
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=6)', setup=timeitSetup, number=100)) # ~ 1.7 sec
    print(timeit.timeit(stmt='integrate_async(math.cos, 0, 1, n_jobs=8)', setup=timeitSetup, number=100)) # ~ 1.25 sec
    
    # One threaad
    print(timeit.timeit(stmt='integrate(math.cos, 0, 1)', setup=timeitSetup, number=100)) # my result 10.3 sec

    # Cpython 
    print(timeit.timeit(stmt='c_integrate(0, 1)', setup=timeitSetup, number=100)) # gil and nogil ~0.47 sec;   

    # Result
    print( integrate(math.cos, 0, 1) )

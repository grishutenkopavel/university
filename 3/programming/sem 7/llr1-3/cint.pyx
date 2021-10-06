from libc.math cimport cos

def c_integrate(float a, float b, float countOfSteps = 10**6) -> float: 
    cdef float result = 0
    cdef float h = 1 / countOfSteps
    cdef float rightBorder = b - h
    with nogil:
        while a <= rightBorder:
            result += (cos(a) + cos(a + h)) / 2
            a += h
    return result * h
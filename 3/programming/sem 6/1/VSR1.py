import numpy as np
import time
import random


startTime = time.time()
n = random.randint(0, 101)
arr1 = np.random.sample((n, n))
arr2 = np.random.sample((n, n))
result = np.dot(arr1, arr2, out=None)
totalTime = time.time() - startTime
print("%s - seconds" % totalTime)
print("%d - size" % n)


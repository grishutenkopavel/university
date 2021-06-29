def fibGenerator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for fib in fibGenerator(20):
    print(fib, end=' ')
print()

def fibonacciLists(n):
    fibonacciNumbers = [0, 1]
    for i in range(2, n+1):
        fibonacciNumbers.append(fibonacciNumbers[-1]+fibonacciNumbers[-2])
    return fibonacciNumbers

print(fibonacciLists(20))
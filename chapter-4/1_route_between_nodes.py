"""
Chapter 4 - Problem 4.1 - Route Between Nodes
Problem:
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

"""


def fibonacci(n):
    if n < 1:
        print('Incorrect input.')

    fib = {1: 0, 2: 1}  # used a dict to memorize the calculated Fibonacci Number
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print(fibonacci(2))
print(fibonacci(8))

def fibonacci2(n):
    if n < 1:
        print('Incorrect input.')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci2(2))
print(fibonacci2(8))
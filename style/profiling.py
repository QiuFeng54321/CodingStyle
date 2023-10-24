import cProfile

def fibonacci_recursive(n):
    if n <= 2: return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    a = 0
    b = 1
    c = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return c

with cProfile.Profile() as pr:
    print(fibonacci_recursive(30))
    print(fibonacci_iterative(30))
    pr.print_stats(sort="tottime")
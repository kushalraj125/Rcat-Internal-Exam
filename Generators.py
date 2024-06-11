def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Example usage
n = 50
for fib in fibonacci_sequence(n):
    print(fib)

# Output: 0 1 1 2 3 5 8 13 21 34

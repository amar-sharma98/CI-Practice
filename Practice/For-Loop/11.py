#Find and print the sum of fib series

def fib_sum(n):
    a, b = 0, 1
    sum_fib = 0
    for i in range(n):
        # print(a, end=",")
        sum_fib += a
        a,b = b, a + b
    return sum_fib
print(fib_sum(10))
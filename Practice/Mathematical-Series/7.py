#Find and print sum of fib series up to required number
#Sum=F(n+2)​−1

def fib(n):
    a,b = 0, 1
    for i in range(n):
        # print(a, end=",")
        a, b = b, a+b
    return a

def sum_fib(n):
    return fib(n + 2) - 1

n = 5

print("sum of first",n, "number of fib is", sum_fib(n))


#Print fibonacci series upton n numbers

def fib(n):
    a, b = 0, 1
    count = 0
    while True:
        if count > n:
            break
        print(a, end=",")
        a, b = b, a + b
        count += 1

fib(10)
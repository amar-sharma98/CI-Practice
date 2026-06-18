#Print fib number row by row where each row prints the next fib numbers

def fib(n):
    a,b = 0, 1
    for i in range(1, n+1):
        for j in range(i):
            print(a, end=" ")
            a, b = b, a + b
        print()

fib(3)

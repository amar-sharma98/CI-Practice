#For every number from 1 to n, count and print total number of it's factors

def factors(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                print(j)
        print("================")
factors(10)
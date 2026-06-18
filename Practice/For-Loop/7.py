#Calculate and print factorial of every number from 1 to n:

def fact_of_every_number(n):

    for i in range(1, n+1, 1):
        result = 1
        for j in range(i, 0, -1):
            result *= j
        print(f"Factorial of {i} is {result}")

fact_of_every_number(5)
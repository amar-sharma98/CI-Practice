#Print all even numbers between 1 to 100

def evenNumbers(n):
    for i in range(1, n+1, 1):
        if i % 2 == 0:
            print(i)

evenNumbers(100)
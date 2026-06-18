#Print all odd numbers between 1 and 100

def oddNumbers(n):

    for i in range(1, n+1, 1):
        if i % 2 != 0:
            print(i)

oddNumbers(100)
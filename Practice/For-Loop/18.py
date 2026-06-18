#Print all numbers between a and b that are divisible by 7

def div_by_seven(a, b):
    if a == 0:
        a = a+1
    for i in range(a, b+1):
        if i % 7 == 0:
            print(i)
div_by_seven(7,30)
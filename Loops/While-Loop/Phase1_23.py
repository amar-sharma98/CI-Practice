#Print all numbers between a and b that are divisable by 7

a = 5
b = 30

while a <= b:
    if a % 7 == 0:
        print(a)
    a += 1
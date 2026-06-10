#Print all factors of the given number

num = 28
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1
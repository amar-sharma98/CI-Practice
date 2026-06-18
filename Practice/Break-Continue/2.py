#Print nums from 1 to 100 but skip nums which are divisible by 5

def skip_5(n):
    for i in range(1, n+1):
        if i % 5 == 0:
            continue
        else:
            print(i)

skip_5(100)
#Print from 1 to 100 and stop as soon as we encounter a number which is divisible by 17

def print_nums(n):
    for i in range(1, n+1):
        if i % 17 == 0:
            break
        else:
            print(i)

print_nums(100)
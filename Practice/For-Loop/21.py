#Finf sum of odd numbers from 1 to n

def sum_of_odd(n):
    sum_odd = 0

    for i in range(n+1):
        if i % 2 != 0:
            sum_odd += i
    return sum_odd

print(sum_of_odd(10))
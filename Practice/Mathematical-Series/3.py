#Find and print sum of n odd numbers

def sum_odd(n):
    sum_odd = 0
    if n > 0:
        sum_odd = n ** 2
        return sum_odd
    else:
        return 0
    
print(sum_odd(5))
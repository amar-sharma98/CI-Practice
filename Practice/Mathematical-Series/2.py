#Find and print sum of first n even numbers

def sum_of_even(n):
    sum_even = 0

    if n > 0:
        sum_even = n * (n + 1)
        return sum_even
    else:
        return 0
    
print(sum_of_even(5))
#Find and print sum of first n natural numbers

def sum_of_natural_numbers(n):
    sum_of_num = 0
    if n > 0:
        sum_of_num = n * (n+1) // 2
        return sum_of_num
    else:
        return 0
    
print(sum_of_natural_numbers(10))
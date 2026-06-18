#Find and print the sum of first n natural numbers

def narural_sum(n):
    sum_of_numbers = 0
    for i in range(n+1):
        sum_of_numbers += i
    return sum_of_numbers

print(narural_sum(10))
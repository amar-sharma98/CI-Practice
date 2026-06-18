#Find and print sum of all even numbers from 1 to n

def sum_of_even(n):
    sum_even = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum_even += i
    return sum_even

print(sum_of_even(10))
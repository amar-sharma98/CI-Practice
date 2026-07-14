#Print all numbers from 1 to 100 whose sum of digits is even

def isEven(num):
    sum_digit = 0
    while num > 0:
        digit = num % 10
        sum_digit += digit
        num //= 10
    if sum_digit % 2 == 0:
        return True
    return False

def print_even_sum_of_digits(range_of_number):
    for i in range(1, range_of_number, 1):
        if isEven(i):
            print(f"Sum of digits of {i} is even")

range_of_number = int(input("Enter a number(n): "))
print_even_sum_of_digits(range_of_number)

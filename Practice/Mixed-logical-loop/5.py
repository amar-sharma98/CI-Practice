#Print all number from 1 to 100 whose sum of digits if multiple of 3

def sum_of_digits(n):
    sum_of_digit = 0
    while n > 0:
        digit = n % 10
        sum_of_digit += digit
        n //= 10
    return sum_of_digit

def print_sum_of_digit_multiple_of_3(end):
    for i in range(1, end+1):
        is_valid_sum = sum_of_digits(i)
        if is_valid_sum % 3 == 0:
            print(f"{i} is multiple of 3")

print_sum_of_digit_multiple_of_3(100)

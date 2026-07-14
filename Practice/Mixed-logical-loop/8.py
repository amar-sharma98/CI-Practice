#Find & print the sum of odd digits & sum of even digits of the given number

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def sum_of_digits(num):
    sum_odd = 0
    sum_even = 0
    while num > 0:
        digit = num % 10
        if is_even(digit):
            sum_even += digit
        else:
            sum_odd += digit
        num //= 10
    print(f"Sum of even digits is : {sum_even}")
    print(f"Sum of odd digits is : {sum_odd}")

sum_of_digits(12345)
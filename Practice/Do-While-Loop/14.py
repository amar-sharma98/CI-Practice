#Summation of all digits of a given number

def sumOfDigits(num):
    digit_sum = 0
    while True:
        if num > 0:
            digit = num % 10
            digit_sum += digit
            num //= 10
        else:
            break
    return digit_sum

print(sumOfDigits(123))
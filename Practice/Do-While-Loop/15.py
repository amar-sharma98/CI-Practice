#Calculate and print sum of even and odd digits seperately of a given number

def calculateSum(num):
    even_sum = 0
    odd_sum = 0
    while True:
        if num > 0:
            digit = num % 10
            if digit % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit
            num //= 10
        else:
            break
    return f"Even Sum: {even_sum} Odd Sum: {odd_sum}"

print(calculateSum(12345678))
#Find the smallest digit in the given number

number = 876868623
current = 9
while number > 0:
    digit = number % 10
    if digit < current:
        current = digit
    number //= 10
print("Smallest digit: ", current)
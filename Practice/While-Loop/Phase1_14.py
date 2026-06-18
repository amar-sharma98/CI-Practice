#Sum of digits of a number

number = 12345
sum = 0

while number > 0:
    sum += number % 10
    number //= 10

print(sum)
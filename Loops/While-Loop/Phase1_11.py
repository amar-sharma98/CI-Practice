#Count and print the total number of digits in the number

number = 12345
counter = 0

while number > 0:
    number //= 10
    counter += 1

print(counter)
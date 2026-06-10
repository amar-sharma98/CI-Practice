#Find the largest digit in the given number

number = 123661790
largest = 0

while number > 0:
    digit = number % 10
    if digit > largest:
        largest = digit
    number //= 10
print("Largest digit: ",largest)
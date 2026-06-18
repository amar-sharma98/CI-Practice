#Reverse the given number and print

number = 54321
reversed = 0

while number > 0:
    digit = number % 10
    reversed = reversed * 10 + digit
    number //= 10
print(reversed)
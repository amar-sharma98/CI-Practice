#Palindrome number

number = 12321
original = number
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10
if reverse == original:
    print("Palindrome")
else:
    print("Not Palindrome")
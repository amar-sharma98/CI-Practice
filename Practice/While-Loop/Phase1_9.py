#Factorial of number "n"

number = int(input("Enter a number: "))
i = 1
result = 1
while i <= number:
    result *= i
    i += 1
print(result)
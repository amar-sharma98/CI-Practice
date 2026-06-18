#FInd and print product of all digits of a given number

number = 1234
product = 1
while number > 0:
    product *= number % 10
    number //= 10
print(product)
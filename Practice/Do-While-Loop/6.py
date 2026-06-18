#Reverse the given number and print

def reverse(num):
    rev = 0

    while True:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        if num == 0:
            break
    return rev

print(reverse(1234))
#Check whether the given number is palindrome

def is_palindrome(num):
    original_num = num
    rev = 0
    while True:
        if num == 0:
            break
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    if original_num == rev:
        return "Palindrome"
    return "Not Palindrome"
print(is_palindrome(12021))
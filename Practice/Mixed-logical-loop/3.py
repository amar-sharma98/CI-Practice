#Print all palindrome numbers between 1 & 500

def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if reversed_num == original_num:
        return True
    return False

def print_palindrome(end):
    for i in range(1, end, 1):
        if is_palindrome(i):
            print(f"{i} is palindrome")

n = 500
print_palindrome(n)
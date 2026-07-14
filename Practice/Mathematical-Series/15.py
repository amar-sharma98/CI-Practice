#Check whether the given number is a strong number, where the number equals the sum of factorials of it's digits
#Ex : 123 = 1! + 2! + 3!

def is_strong_number(n):
    original_num = n
    result = 0
    
    while n > 0:
        digit = n % 10
        result += factorial(digit)
        n //= 10
    if result == original_num:
        return True
    return False

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

n = int(input("Enter a number(n): "))
print(is_strong_number(n))
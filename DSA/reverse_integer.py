#Reverse Integer -- LC

def reverse_int(nums):
    result = 0
    INT_MAX = (2**31)-1
    n = abs(nums)
    while n != 0:
        digit = n % 10
        limit = 7 if nums >= 0 else 8
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > limit):
            return 0
        result = result * 10 + digit
        n //= 10
    if nums < 0:
        return result * -1
    else:
        return result
print(reverse_int(80000))

def reverse(num):
    n = abs(num)
    rev = 0

    while(n != 0):
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    if num < 0:
        rev = -rev
    if (rev >= -2**31 and rev <= 2**31 -1):
        return rev
    return 0

print(reverse(-2147483648))
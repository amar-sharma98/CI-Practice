#Find the LCM of the given numbers


#Brute Force

def lcm(a, b):
    maximum = max(a, b)
    while True:
        if maximum % a == 0 and maximum % b == 0:
            return maximum
        maximum += 1
print(lcm(2, 4))   # 8
########################################
#Using HCF to find lcm : LCM(a, b) = (a * b) / HCF(a, b)
def lcm(num1, num2):
    if num1 == 0 or num2 == 0:
            return 0
    return (num1 * num2) // hcf(num1, num2)

def hcf(num1, num2):
    result = 1
    minimum = min(num1,num2)
    if num1 > 0 and num2 > 0:
        for i in range(1, minimum + 1):
            if num1 % i == 0 and num2 % i == 0:
                result = i
    return result

print(lcm(4, 8))

#Using built in gcd
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(5, 11))   # 8
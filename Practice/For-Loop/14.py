#Find HCF of the given numbers
def hcf(num1, num2):
    result = 1
    minimum = min(num1,num2)
    if num1 > 0 and num2 > 0:
        for i in range(1, minimum + 1):
            if num1 % i == 0 and num2 % i == 0:
                result = i
    return result
print(hcf(4,8))

#Optimized
def hcf(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


print(hcf(4, 8))   # 4
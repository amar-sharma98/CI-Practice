#Find the HCF of the given two numbers

num1 = 36
num2 = 60
hcf = 1
i = 1
while i <= min(num1, num2):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
    i += 1
print(hcf)

#Optimized
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6
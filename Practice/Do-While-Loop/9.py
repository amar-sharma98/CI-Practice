#Calculate and print the factorial oof the given number.
def fact(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    while num != 0:
        fact *= num
        num -= 1
    return fact
print(fact(5))

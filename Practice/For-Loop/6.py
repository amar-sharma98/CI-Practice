#Calculate and print factorial of given number "n"

def fact(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print(fact(5))
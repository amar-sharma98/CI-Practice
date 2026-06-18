#Check whether the given number is prime or not

def isPrime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

print(isPrime(3))
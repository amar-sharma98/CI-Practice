#Print all "Armstrong number" between 1 & 1000

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    if total == n:
        return True
    return False


def print_armstrong(end):
    for i in range(1, end+1):
        if is_armstrong(i):
            print(f"{i} is a Armstrong number")

print_armstrong(1000)
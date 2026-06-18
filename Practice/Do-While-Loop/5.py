#Count and print the number of digits in the given number

def count_digit(num):
    if num == 0:
        return 1
    count = 0
    while num:
        count += 1
        num //= 10
    return count

print(count_digit(1234))
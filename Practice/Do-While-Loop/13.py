##Keep taking number from user until a negative number is entered and print the count of positive number##

def countPositiveNumbers():
    count = 0
    while True:
        num = int(input("Enter a nuber: "))
        if num >= 0:
            count += 1
        else:
            break
    return count

print('Positive Number Count: ', countPositiveNumbers())
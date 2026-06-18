#Check whether the given number is armstrong or not

def armstrong(num):
    original_num = num
    square = 0
    n = len(str(num))
    while True:
        if num == 0:
            break
        digit = num % 10
        square += digit ** n
        num //= 10
    return True if original_num == square else False
print(armstrong(153))

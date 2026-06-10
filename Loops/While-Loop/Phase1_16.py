#Perfect number or nut

number = 28
i = 1
sum_divisor = 0

while i <= number//2 :
    if number % i == 0:
        sum_divisor += i
    i += 1

if sum_divisor == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
#Armstrong number or not
number = 153
original = number
num_length = len(str(number))
arm_num = 0
while number > 0:
    digit = number % 10
    arm_num += digit ** num_length
    number //= 10
if arm_num == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
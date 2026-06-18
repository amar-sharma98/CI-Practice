#Keep taking numbers from user until user enters "0", and print the sum


sum_num = 0
while True:
    num = int(input("Enter the number: "))
    sum_num += num
    if num == 0:
        break
print("Sum of numbers: ", sum_num)
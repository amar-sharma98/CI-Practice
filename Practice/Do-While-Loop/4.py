#Keep taking numbers from user until user enters "0", and print the largest number


largest = 0
while True:
    num = int(input("Enter the number: "))
    if num == 0:
        break
    elif num > largest:
        largest = num
print("Largest number: ", largest)
#Keep taking number form user and print untill a negative number comes, if nuber is -ve braek the loop

def negative_break():
    while True:
        num = int(input("Enter a number: "))
        if num >= 0:
            print(f"Number is {num}")
        else:
            break

negative_break()
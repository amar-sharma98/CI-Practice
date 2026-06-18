#Skip all odd nums and print only even

def skip_odd():
    while True:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(num)
        elif num < 0:
            break
        else:
            continue
skip_odd()
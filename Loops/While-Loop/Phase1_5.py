#Print multiplication table of "N"

number = int(input("Enter the number: "))
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
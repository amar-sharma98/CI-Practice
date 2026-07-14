#Print stars and spaces alternating (stars and blank spaces)

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print("*" if j % 2 == 1 else " ", end="")
    print()

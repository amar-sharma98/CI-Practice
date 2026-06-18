#Print number triangle using nested loops

def number_triangle(rows):
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()
number_triangle(5)

def pattern2(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

pattern2(4)

def floyd(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

floyd(4)

def inverted(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i + 1):
            print(i, end=" ")
        print()

inverted(4)

def right_aligned(rows):
    for i in range(1, rows + 1):
        print("  " * (rows - i), end="")
        for j in range(i):
            print(i, end=" ")
        print()

right_aligned(4)

def pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(2 * i - 1):
            print(i, end="")
        print()

pyramid(3)

def binary(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print((i + j) % 2, end=" ")
        print()

binary(4)

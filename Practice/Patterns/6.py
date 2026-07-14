#Print a right angle triangle of stars

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
#Print stars in an even numbers (2, 4, 6, 8, ...)

rows = 10

for i in range(rows + 1):
    if i % 2 == 0:
        print(i * "*")
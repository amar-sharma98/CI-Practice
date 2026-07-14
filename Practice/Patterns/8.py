#Print stars in odd numbers (1, 3, 5, 7, ....)

rows = 10

for i in range(rows + 1):
    if i % 2 != 0:
        print(i * "*")
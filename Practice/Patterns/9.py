#Print a centered pyramid of stars

rows = 10

for i in range(rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)

    print(spaces + stars)
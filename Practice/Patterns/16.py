rows = 5
ch = ord('A')

for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

        if ch > ord('Z'):
            ch = ord('A')

    print()
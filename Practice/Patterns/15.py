#
rows = 7
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
        if num > 1:
            num = 0
    print()
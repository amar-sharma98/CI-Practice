#Print a pattern where ith row prints the value of i x i

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i * i, end=" ")
    print()
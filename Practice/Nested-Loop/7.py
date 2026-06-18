#Print a matrix, then calculate and display the sum of each row  and the sum of each column

def sum_matrix(n, m):
    matrix = []

    # Create and print matrix
    print("Matrix:")
    for i in range(1, n+1):
        row = []
        for j in range(1, m+1):
            value = i * j   # generating matrix values
            row.append(value)
            print(value, end=",")
        matrix.append(row)
        print()

    # Row sums
    print("\nRow sums:")
    for i in range(n):
        print(f"Row {i+1} sum =", sum(matrix[i]))

    # Column sums
    print("\nColumn sums:")
    for j in range(m):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        print(f"Column {j+1} sum =", col_sum)


# Example call
sum_matrix(4, 8)

def print_matrix(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i * j, end=" ")   # value of matrix
        print()  # move to next row

print_matrix(4, 5)
#Print pair of (i,j) from 1 to n

def pairs(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(f"(i, j) = {i, j}")
    print("====================")

pairs(10)
#Calculate and print the value of series 1^3 + 2^3 + 3^3 + .... n^3
#Formula: Sum : ((n(n+1)/2​) ^ 2

def sum_cubes(n):
    return int((n * (n + 1) / 2) ** 2)
print(sum_cubes(5))
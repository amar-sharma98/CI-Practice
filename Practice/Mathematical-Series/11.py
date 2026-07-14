#Print the series of powers of 2 ==> 2 ^ 1 + 2 ^ 2 + .... + 2 ^ n
#Sum : (2 ^ n+1)-2

def sum_of_power_two(n):
    result = 0
    for i in range(1, n+1):
        result  = (2 ** (n + 1)) - 2
    return result
print(sum_of_power_two(10))

def print_series(n):
    for i in range(1, n+1):
        print(f"2^{i}", end=" + ")
print_series(10)

############################################
n = int(input("Enter value of n: "))

for i in range(1, n + 1):
    print(f"2^{i}", end=" + " if i < n else "")
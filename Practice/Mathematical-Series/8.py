#Calculate and print the value of series 1^2 + 2^2 + 3^2 + .... n^2
#Formula: Sum : (n(n+1)(2n+1)​)/6
def calculate_sum(n):
    return (n * (n + 1) * (2 * n + 1))//6
print(calculate_sum(5))


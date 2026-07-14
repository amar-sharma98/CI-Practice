#Print all perfect nmber betwen 1 and 1000

def is_number_perfect(n):
    sum_of_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_factors += i
    if sum_of_factors == n:
        return True
    return False

def print_perfect_numbers(end):
    for i in range(1, end+1):
        if is_number_perfect(i):
            print(f"{i} is a perfect number")

print_perfect_numbers(1000)
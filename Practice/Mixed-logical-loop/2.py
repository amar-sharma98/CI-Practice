#Count total numbers between 1 & 500 that are divisible by 7 but not by 5

def count_numbers(end):
    count = 0
    for i in range(1, end, 1):
        if i % 7 == 0 and i % 5 != 0:
            count += 1
    return count

n = 500
print(count_numbers(500))
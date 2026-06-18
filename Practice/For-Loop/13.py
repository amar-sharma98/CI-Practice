#Find and print sum of all factors of a given nubber

def som_of_factors(num):
    fact_sum = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            fact_sum += i
            if i != num // i:
                fact_sum += num // i
    return fact_sum

print(som_of_factors(10))
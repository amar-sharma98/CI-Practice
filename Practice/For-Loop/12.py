#Print all factors of the given number

def factors(num):
    factors_list = []
    for i in range(1, (num//2) +1):
        if num % i == 0:
            factors_list.append(i)
    factors_list.append(num)
    return factors_list

print(factors(100))

#Optimized
def factors_opt(num):
    factors_list = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors_list.append(i)
            if i != num // i:
                factors_list.append(num // i)
    return sorted(factors_list)
print(factors_opt(10))
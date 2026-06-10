#Print all prime number from 1 to 100

num = 1
while num <= 100:
    if num > 1:   # primes are greater than 1
        i = 2
        is_prime = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i+=1
        
        if is_prime:
                    print(num, end=" ")

    num += 1


#Print all prime number between 1 and 100

def primes_upto_n(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    for i in range(2, n + 1):
        if sieve[i]:
            print(i, end=" ")


primes_upto_n(100)
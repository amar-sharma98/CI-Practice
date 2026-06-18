#Print all prime numbers upto n using nested-loop checking

# Print all prime numbers up to n using nested loops

def print_primes(n):
    for num in range(2, n + 1):      # outer loop: numbers from 2 to n
        is_prime = True

        for i in range(2, num):      # inner loop: check divisibility
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")


print_primes(50)
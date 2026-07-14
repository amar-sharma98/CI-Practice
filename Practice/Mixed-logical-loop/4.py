#Get the list of integer from user (Input) and retrive the prime numbers from list and print the  sum of alternate prime numbers from new list

def is_prime(n):

    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def retrive_prime_from_list(list_input):
    prime_list = []
    length = len(list_input)
    for i in range(length):
        if is_prime(list_input[i]):
            prime_list.append(list_input[i])
    return prime_list

def sum_of_alternate_prime(list_input):
    prime_list = retrive_prime_from_list(list_input)
    length = len(prime_list)
    sum_of_prime = 0
    for i in range(0, length, 2):
        sum_of_prime += prime_list[i]
    return sum_of_prime

list_input = list(map(int, input("Enter a list of numbers seperated by comma(,): ").split(',')))
print(sum_of_alternate_prime(list_input))


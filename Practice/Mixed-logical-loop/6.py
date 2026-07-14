#Print all numbers from 1 to n whose binary representation contains an even number of 1s.

def binary_conversion(n):
    binary = bin(n)[2:]
    return binary

def count_ones(n):
    binary = binary_conversion(n)
    count = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            count += 1
    if count % 2 == 0:
        print(binary)

def print_all_binaries(end):
    for i in range(1, end+1):
        count_ones(i)

print_all_binaries(100)
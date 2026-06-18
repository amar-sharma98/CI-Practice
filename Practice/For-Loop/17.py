#Cube of each number from 1 to n

def cube_of_number(n):
    for i in range(1, n+1):
        print(f"Cube of {i} is : {i ** 3}")
cube_of_number(10)
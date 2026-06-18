#Print the miltiplication table of given number

def mult(n):
    for i in range(1, 10 + 1, 1):
        print(f"{n} x {i} = {n * i}")

mult(3)
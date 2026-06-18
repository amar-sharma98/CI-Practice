#Print all pythagorean triplets whose values are less than or equal to n

def pythagorian_triplets(n):
    print("Pythagorean Triplets:")

    for a in range(1, n+1):
        for b in range(a, n+1):   # start from 'a' to avoid duplicates
            for c in range(b, n+1):
                if a*a + b*b == c*c:
                    print(a, b, c)

# Example call
pythagorian_triplets(10)
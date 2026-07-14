#calculate and print the value of the series:
#1! + 2! + 3! + ..... + n!

n = int(input("Enter value of n: "))

fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i          # Calculate i!
    total += fact      # Add to sum
    print(f"{i}! = {fact}")

print("Sum =", total)
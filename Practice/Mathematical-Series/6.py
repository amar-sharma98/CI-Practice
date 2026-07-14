#Print Fibonacci series up to the required number of terms
#F(n)=F(n−1)+F(n−2)

n = int(input("Enter number of terms(n): "))
a,b = 0, 1

for i in range(n):
    print(a, end=",")
    a, b = b, a+b
print()
#Recursive method using : F(n)=F(n−1)+F(n−2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first n terms
n = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")
#Print Fibonacci series upto "n" terms

n = 10   # number of terms

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

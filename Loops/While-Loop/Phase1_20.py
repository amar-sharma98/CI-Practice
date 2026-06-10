#Sum of Fib series upto n terms
n = 10   # number of terms

a, b = 0, 1
count = 0
sum_fib = 0
while count < n:
    sum_fib += a
    a, b = b, a + b
    count += 1
print(sum_fib)
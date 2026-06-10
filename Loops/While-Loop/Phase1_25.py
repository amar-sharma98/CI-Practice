#Find and print sum of all factors of the given number

num = 30
i = 1
sum_fact = 0
while i <= num:
    if num % i == 0:
        # print(i)
        sum_fact += i
    i += 1
print(sum_fact)
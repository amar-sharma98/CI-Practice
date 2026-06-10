#Check whether the given number is prime or not

num = int(input("Enter a number: "))
i = 1
count = 0

while num >= i:
    if num % i ==0:
        count += 1
    i += 1
if count > 2:
    print("Not Prime")
else:
    print("Prime")
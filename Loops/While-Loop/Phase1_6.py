#Sum of first "n" natural numbers

end = int(input("Enter a number: "))
i = 0
result = 0
while i <= end:
    result  += i
    i += 1
print(f"Sum of {end} natural numbers from 0 is {result}")
#Calculate the sum of odd number from 1 to "n"

end  = int(input("Enter a number: "))
start = 0
result  = 0
while start <= end:
    if start % 2 != 0:
        result += start
    start += 1
print(result)
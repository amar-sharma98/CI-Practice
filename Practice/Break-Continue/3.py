#Take 5 numbers as input, skip any number that is 0 using continue and calculate sum of remaining numbers

def sum_of_nums():
    sum_is = 0
    for _ in range(5):
        num = int(input("Enter a number: "))
        if num == 0:
            continue
        else:
            sum_is += num
    return sum_is

print(sum_of_nums())
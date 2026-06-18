#Continuously add numbers in a loop and stop when number becomes >100

def break_loop():
    sum_num = 0
    while True:
        num = int(input("Enter a number: "))
        sum_num += num

        if sum_num > 100:
            break
    return sum_num

print(break_loop())
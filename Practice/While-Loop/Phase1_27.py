#Find LCM of two given numbers

a = 4
b = 6

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        print("LCM:", max_num)
        break
    max_num += 1
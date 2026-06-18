#Search for a specific number in a list and terminate the loop immidiately when the number is found

def search_num(num):
    num_list = [1, 2, 3, 10, 1, 2, 2]
    for i in range(len(num_list)):
        print(num_list[i])
        if num_list[i] == num:
            print(f"Found {num}")
            break
    
search_num(1)
#Another way
def search_num(num):
    num_list = [1, 2, 3, 10, 1, 2, 2]

    if num in num_list:
        print(f"Found {num}")
    else:
        print(f"{num} not found")

search_num(10)
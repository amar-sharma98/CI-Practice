#Move all "0" to the end

def move_zeros_end(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] , arr[j] = arr[j] , arr[i]
            i += 1
    return arr

arr = [1, 0, 2, 3, 0, 8, 0]
print(move_zeros_end(arr))

#Move all zeron in front
def move_zeros_front(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            arr[i] , arr[j] = arr[j] , arr[i]
            i += 1
    return arr

arr = [1, 0, 2, 3, 0, 8, 0]
print(move_zeros_front(arr))
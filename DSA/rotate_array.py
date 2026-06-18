#Reverse an array right by 2
def rotate_array_left(arr, k):
    n = len(arr)
    k = k % n

    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

    return arr

print(rotate_array_left([1, 2, 3, 4, 5], 2))

#Rotate array left by 2
def rotate_array_left(arr, k):
    n = len(arr)
    k = k % n

    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
    reverse(0, k-1)
    reverse(k, n-1)
    reverse(0, n-1)

    return arr

print(rotate_array_left([1, 2, 3, 4, 5], 2))
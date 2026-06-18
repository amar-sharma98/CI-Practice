def majority(arr):
    candidate = 0
    count = 0

    # Find candidate
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


print(majority([2, 2, 2, 1, 2, 1, 5]))
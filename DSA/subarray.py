def longest_with_at_most_k(arr, target, k):
    left = 0
    count = 0
    max_len = 0

    for right in range(len(arr)):
        if arr[right] == target:
            count += 1

        while count > k:
            if arr[left] == target:
                count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def largest_subarray(arr):
    return max(
        longest_with_at_most_k(arr, 0, 2),  # at most 2 zeros
        longest_with_at_most_k(arr, 1, 2)   # at most 2 ones
    )


arr = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
print(largest_subarray(arr))
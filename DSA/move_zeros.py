#Move zeros to front

def movezeros_front(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
print(movezeros_front([0, 1, 2, 0, 3, 0, 8, 0]))


def movezeros_end(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
    return nums

print(movezeros_end([9, 0, 1, 2, 0, 3, 0, 8, 0]))

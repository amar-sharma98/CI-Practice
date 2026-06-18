#Find an element in array whose occurance is n/2 in an array

def occurance(nums):
    element = None
    count  = 0

    for num in nums:
        if count == 0:
            element = num
        if num == element:
            count += 1
        else:
            count -= 1
    return element

print(occurance([1,2, 3, 1, 1, 2]))

    


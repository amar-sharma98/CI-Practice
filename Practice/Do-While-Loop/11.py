#FInd HCF of the given numbers


def hcf_no(nums):
    minNum = minimum(nums)
    result = 1

    for i in range(1, minNum + 1):
        is_hcf = True
        for num in nums:
            if num % i != 0:
                is_hcf = False
                break

        if is_hcf:
            result = i

    return result

def minimum(nums):
    minNum = nums[0]   # start with first element
    for num in nums:
        if num < minNum:
            minNum = num
    return minNum
print(hcf_no([2, 4, 6, 8]))
print(hcf_no([2, 4, 6, 9]))   # 2

#Optimized
def hcf(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
        if result == 1:     # early exit optimization
            return 1

    return result


print(hcf([2, 4, 6, 8]))   # 2
print(hcf([2, 4, 6, 9]))   # 1
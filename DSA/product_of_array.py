#Product of array except itself

def product(nums):
    n = len(nums)
    product = [1] * n

    prefix = 1
    for i in range (n):
        product[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n-1, -1, -1):
        product[i] *= suffix
        suffix *= nums[i]
    return product

print(product([1, 2, 3, 4]))

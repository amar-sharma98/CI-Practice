
# Given a list of integers, find the unique element that appears only once while all other elements appear twice.
#Not optimized solution using Counter from collections module
# from collections import Counter
# class Solution:
#     def unique_element(self, nums : list):
#         count = Counter(nums)
#         for n, c in count.items():
#             if c == 1:
#                 return n
#         return None

# sol = Solution()
# print(sol.unique_element([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

# Optimized solution using XOR operator
class Solution:
    def unique_element(self, nums:list):
        unique = 0
        for num in nums:
            unique ^= num
        return unique
    
sol = Solution()
print(sol.unique_element([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]))

#optimized solution using set
# class Solution:
#     def unique_element(self, nums:list):
#         unique = set()
#         for num in nums:
#             if num in unique:
#                 unique.remove(num)
#             else:
#                 unique.add(num)
#         return unique.pop() if unique else None
# sol = Solution()
# print(sol.unique_element([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]))

#Solution for multiple unique elements
# def unique_elements(numbers):
#     seen = set()
#     duplicates = set()
#     for num in numbers:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)
#     return list(seen - duplicates)
# print(unique_elements([1, 2, 2, 3, 1, 4]))

def unique(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(seen - duplicates)

print(unique([1, 2, 2, 3, 3, 4]))

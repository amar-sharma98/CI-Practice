# Function to find two numbers that add up to a target sum
#Not the most efficient solution, but it works for small lists. For larger lists, consider using a hash map to store the numbers and their indices for faster lookups.
# def two_sum(numbers, target):
#     num_dict = {}
#     for i, num in enumerate(numbers):
#         complement = target - num
#         if complement in num_dict:
#             return (num_dict[complement], i)
#         num_dict[num] = i
#     return None
# # Example usage
# numbers = [2, 11, 15, 7]
# target = 9
# result = two_sum(numbers, target)
# if result:
#     print(f"Indices of the two numbers that add up to {target}: {result}")


#Optimized version using two-pointer technique (only works if the list is sorted)
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
# Example usage for sorted list
sorted_numbers = [2, 7, 11, 15]
target = 9
result = two_sum_sorted(sorted_numbers, target)
if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")


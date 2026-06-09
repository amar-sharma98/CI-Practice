#Optimize code to find duplicate element
def duplicates_element(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
print(duplicates_element([1, 2, 2, 3, 3, 4]))

#Code to return duplicates only
def duplicate_word(input_string):
    words = input_string.lower().split()
    seen = set()
    duplicates = []
    for word in words:
        if word in seen:
            duplicates.append(word)
        else:
            seen.add(word)
    return list(duplicates)
input_string = "Hello World Test hello world"
print(duplicate_word(input_string))
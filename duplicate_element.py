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

def process_words(words):
    count = {}
    result = []
    first_duplicate_word = None

    for word in words:
        if word not in count:
            count[word] = 1
            result.append(word)
        else:
            count[word] += 1

            # Identify first duplicate word
            if first_duplicate_word is None:
                first_duplicate_word = word
                result.append(word)

            # Allow ALL occurrences of that first duplicate word
            elif word == first_duplicate_word:
                result.append(word)

            # Ignore duplicates of other words
            else:
                continue

    return result


# Test
words = ["orange", "apple", "banana", "cherry", "apple", "banana", "date", "cherry", "apple"]
print(process_words(words))
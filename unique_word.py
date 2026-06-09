#Write a program to find the unique words in a given string and return them without changing the order of the words. For example, if the input string is "hello world hello", the output should be "world".
#Not optimized solution
def unique_words(input_string):
    words = input_string.split()
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    return ' '.join(unique)
# Example usage:
input_string = "hello world hello"
print(unique_words(input_string))

#Optimized solution using a set to track seen words
def unique_words(input_string):
    words = input_string.split()
    seen = set()
    unique = []
    for word in words:
        if word not in unique:
            seen.add(word)
            unique.append(word)
    return ' '.join(unique)
# Example usage:
input_string = "hello world hello hello amar world hello"
print(unique_words(input_string))
#Normal approach
# def palindrome(word):
#     result = ''.join(reversed(word.lower()))
#     if word == result:
#         print("Anagram")
#     else:
#         print("Not Anagram")
# palindrome("madam")

# #Optimized --not perfect
# def palindrome_opt(text):
#     word = text.lower()
#     left, right = 0 , len(word)-1

#     while left < right:
#         if word[left] == word[right]:
#             left +=1
#             right -=1
#             return "Palindrome"
#         else:
#             return "Not Palindrome"

# print(palindrome_opt("Madam"))

#Optimized and perfect
def palindrome_opt(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return "Not Palindrome"
        left += 1
        right -= 1

    return "Palindrome"

print(palindrome_opt("madam"))
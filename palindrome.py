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

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num = abs(x)
        reverse = 0
        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10
        return x == reverse
print(isPalindrome(10))

#Optimized
def isPalindrome(x):
    # Negative numbers or ending with 0 (except 0 itself)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0

    # Build reversed second half
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x //= 10

    # For even digits: x == reversed_half
    # For odd digits: x == reversed_half // 10
    return x == reversed_half or x == reversed_half // 10


print(isPalindrome(121))   # True
print(isPalindrome(10))    # False
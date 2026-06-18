# def is_anagram(s1, s2):
#     s1 = s1.lower()
#     s2 = s2.lower()

#     if len(s1) != len(s2):
#         return False

#     freq = [0] * 26

#     for i in range(len(s1)):
#         freq[ord(s1[i]) - ord('a')] += 1
#         freq[ord(s2[i]) - ord('a')] -= 1

#     return all(count == 0 for count in freq)


# # Example
# print(is_anagram("Listen", "Silent"))


def group_anagrams(words):
    anagram_map = {}

    for word in words:
        # Step 1: frequency array
        count = [0] * 26

        for ch in word:
            index = ord(ch) - ord('a')
            count[index] += 1

        # Step 2: convert to key (string)
        key = ""
        for num in count:
            key += str(num) + "#"

        # Step 3: store in hashmap
        if key in anagram_map:
            anagram_map[key].append(word)
        else:
            anagram_map[key] = [word]

    return list(anagram_map.values())


# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
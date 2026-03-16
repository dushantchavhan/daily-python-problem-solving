# Day 11 - Check if two strings are anagrams

def is_anagram(str1, str2):
    # remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # compare sorted characters
    return sorted(str1) == sorted(str2)


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
word1 = "listen"
word2 = "silent"
print("Are anagrams:", is_anagram(word1, word2))

# Test Case 2
word3 = "triangle"
word4 = "integral"
print("Are anagrams:", is_anagram(word3, word4))

# Test Case 3
word5 = "hello"
word6 = "world"
print("Are anagrams:", is_anagram(word5, word6))

# Test Case 4
word7 = "Dormitory"
word8 = "Dirty room"
print("Are anagrams:", is_anagram(word7, word8))
# Day 3 - Palindrome Check
# Checking if a string reads the same forward and backward

def is_palindrome(text):
    text = text.lower()   # convert to lowercase
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
word1 = "madam"
print("Test Case 1:", word1, "->", is_palindrome(word1))

# Test Case 2
word2 = "racecar"
print("Test Case 2:", word2, "->", is_palindrome(word2))

# Test Case 3
word3 = "python"
print("Test Case 3:", word3, "->", is_palindrome(word3))

# Test Case 4 (mixed case)
word4 = "Level"
print("Test Case 4:", word4, "->", is_palindrome(word4))

# Test Case 5 (single character)
word5 = "a"
print("Test Case 5:", word5, "->", is_palindrome(word5))
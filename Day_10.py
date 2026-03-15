# Day 10 - Count vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
text1 = "Hello World"
print("Vowel count:", count_vowels(text1))

# Test Case 2
text2 = "Python Programming"
print("Vowel count:", count_vowels(text2))

# Test Case 3
text3 = "BCDFG"
print("Vowel count:", count_vowels(text3))

# Test Case 4
text4 = ""
print("Vowel count:", count_vowels(text4))
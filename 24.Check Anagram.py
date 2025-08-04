def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Check and print
print("Are anagrams?", is_anagram(str1, str2))

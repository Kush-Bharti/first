## Check if Two Strings are Anagerams.

def is_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return "It is an Anagram"
    else:
        return "Not an Anagram"

data1 = input("Enter First word.:")
data2 = input("Enter Second Word.: ")

print(is_anagram(data1,data2))
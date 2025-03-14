
## Find the first Non-Repeating Character.

characters = input("Enter Character.: ")

repeated = ""
not_repeated = ""

for char in characters:
    if char not in not_repeated:
        not_repeated += char
    else:
        repeated += char
        
print(repeated[0])
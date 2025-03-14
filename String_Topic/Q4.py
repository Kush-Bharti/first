
## Remove the repeated Characters.

character = input("Enter Characters.: ")

result = ""

for i in character:
    if i not in result:
        result += i 

print(result)
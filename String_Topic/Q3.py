## Count Vowels in the given String.

User_input =input("Enter the Strings.: ").lower()
vowels = ['a','e','i','o','u']

sum = 0
for vow in User_input:
    if vow in vowels:
        sum +=1
    
print(sum)

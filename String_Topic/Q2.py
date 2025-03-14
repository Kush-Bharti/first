# Check if a String is Palindrome ...


str = input("Enter the Character ,which you want to check ,Palindrome?.: ")
copy_str = str[::-1]

if str == copy_str:
    print(f"Enter String {str}")
    print(f"Copy of the string {copy_str}")
    print("Is a palindrome")
else:
    print(f"Enter String {str}")
    print(f"Copy of the string {copy_str}")
    print("Not a Palindrome")

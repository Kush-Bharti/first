
str = "hello,Coders,developers,Host"


str1 = str.endswith('st') #Return True if string ends with substr.
print(str1,"\n")

capital_string = str.capitalize() # Capitalizes 1st Char.
print(capital_string,"\n")

replace_string = str.replace("Coders","Pro Coder")  # Replace all the Occurrences of Old value with New value.
print(replace_string,"\n")

find_idx_str = str.find('d')  # Return the 1st index of 1st Occurrence
print(find_idx_str,'\n')

count_str = str.count("o") # Return the no.of element.
print(count_str,'\n')
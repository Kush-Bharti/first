
####   Find the maximum and minimum in the list.

def find_max_min(val):
    return f'Maximum & Minmum No. in the List is {max(val)},{min(val)}'

def sum_of_list(val):
    return sum(val)

value = [9,4,6,5,3,7,1,2]

print(find_max_min(value))
print(f'Sum of the List {sum_of_list(value)}')
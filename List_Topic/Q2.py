
## Find the Second Largest No. in the List.

def largest_no(ls):
    ls.sort(reverse = True)
    unique_list = []
    for i in ls:
        if i not in unique_list:
            unique_list.append(i)
    if len(unique_list) > 1 :
        return f' Second Largest No. of List {ls} is {unique_list[1]} '
    list_copy = ls.copy()
    
    # return f'{list_copy} & {unique_list}'

list = [85,65,95,954,645,5,465,1,954]

print(largest_no(list))

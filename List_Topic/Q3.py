

###  Remove Duplicates from the List (Preserving Order)


def remove_duplicates(st):
    list_updated = set(st)
    lssst = list(list_updated)
    return f'{list_updated} & {lssst}'

value = [8,4,5,1,4,2,6,3,5,8,7,5,4,6,2,3,7]

print(remove_duplicates(value))

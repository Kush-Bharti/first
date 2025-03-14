## Merge 2 sorted lists into 1 Sorted list.

def merge(u1,u2):
    con1 = list(sorted(set(u1)))
    con2 = list(sorted(set(u2)))
    combine = con1 + con2
    return combine
    
user1 = input("Enter The 1. Numbers.: ").split()
user2 = input("Enter The 2. Numbers.: ").split()

print(merge(user1,user2))

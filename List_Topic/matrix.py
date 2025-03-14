
m = int(input("Enter the Row.: ")) # Row
n = int(input("Enter the Cols.: ")) # Col

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        element = input("Enter Element in the matrix.: ")
        row.append(element)
    matrix.append(row)
    
print(matrix)


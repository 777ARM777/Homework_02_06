m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(input())
for i in range(m):
    print(matrix[i])

for i in range(m):
    for j in range(m - i):
        matrix[i][j], matrix[m - i - 1][n - j - 1] = matrix[m - i - 1][n - j - 1], matrix[i][j]
for i in range(m):
    print(matrix[i])

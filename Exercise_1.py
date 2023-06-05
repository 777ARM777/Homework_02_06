matrix = [[0, 'M', 0, 'M', 0],
          [0, 0, 'M', 0, 0],
          [0, 0, 0, 0, 0],
          ['M', 'M', 0, 0, 0],
          [0, 0, 0, 'M', 0]]

for i in range(5):
    for j in range(5):
        sum = 0
        if matrix[i][j] != 'M':
            if i != 0:
                if matrix[i - 1][j] == 'M':
                    sum += 1  # top
                if j != 0:
                    if matrix[i - 1][j - 1] == 'M':
                        sum += 1  # left-top
                if j != 4:
                    if matrix[i - 1][j + 1] == 'M':
                        sum += 1  # right-top
            if i != 4:
                if matrix[i + 1][j] == 'M':
                    sum += 1  # bottom
                if j != 0:
                    if matrix[i + 1][j - 1] == 'M':
                        sum += 1  # left-bottom
                if j != 4:
                    if matrix[i + 1][j + 1] == 'M':
                        sum += 1  # right-bottom
            if j != 0:
                if matrix[i][j - 1] == 'M':
                    sum += 1  # left
            if j != 4:
                if matrix[i][j + 1] == 'M':
                    sum += 1  # right
            matrix[i][j] = sum
print(matrix)

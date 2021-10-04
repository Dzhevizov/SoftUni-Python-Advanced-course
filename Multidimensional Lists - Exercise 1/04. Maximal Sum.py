import sys

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

max_sum = -sys.maxsize
max_submatrix = []

for i in range(rows - 2):
    for j in range(cols - 2):
        sum_submatrix = 0
        submatrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], \
                     [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], \
                     [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
        for x in range(len(submatrix)):
            for y in range(len(submatrix)):
                sum_submatrix += submatrix[x][y]
        if sum_submatrix > max_sum:
            max_sum = sum_submatrix
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
for x in range(len(max_submatrix)):
    for y in range(len(max_submatrix)):
        print(max_submatrix[x][y], end=" ")
    print()

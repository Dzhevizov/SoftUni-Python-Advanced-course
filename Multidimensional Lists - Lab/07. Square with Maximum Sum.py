import sys

rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

max_sum = -sys.maxsize
max_submatrix = []

for i in range(rows - 1):
    for j in range(cols - 1):
        submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
        sum_submatrix = 0
        for line in submatrix:
            sum_submatrix += sum(line)
        if sum_submatrix > max_sum:
            max_sum = sum_submatrix
            max_submatrix = submatrix

for i in range(2):
    for j in range(2):
        print(max_submatrix[i][j], end=" ")
    print()

print(max_sum)

rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for i in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(col_sum)

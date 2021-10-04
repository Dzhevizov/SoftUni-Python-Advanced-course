rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    line = input().split()
    matrix.append(line)

count = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            count += 1

print(count)

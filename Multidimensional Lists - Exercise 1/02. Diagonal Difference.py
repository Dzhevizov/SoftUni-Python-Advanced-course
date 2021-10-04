size = int(input())

matrix = []

for _ in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)

primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size - 1 - i])

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)

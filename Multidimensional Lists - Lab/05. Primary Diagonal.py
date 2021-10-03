size = int(input())

sum_primary = 0

matrix = []

for _ in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for i in range(size):
    sum_primary += matrix[i][i]

print(sum_primary)

rows, cols = [int(x) for x in input().split()]

matrix = [[None for c in range(cols)] for r in range(rows)]

for r in range(rows):
    for c in range(cols):
        matrix[r][c] = chr(97 + r) + chr(97 + r + c) + chr(97 + r)

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=" ")
    print()

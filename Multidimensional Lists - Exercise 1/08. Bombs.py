size = int(input())

matrix = []

for _ in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)

bombs = input().split()
for i in range(len(bombs)):
    r, c = map(int, bombs[i].split(","))
    bombs[i] = (r, c)

for bomb in bombs:
    x = bomb[0]
    y = bomb[1]

    if x not in range(size) and y not in range(size):
        continue

    curr_bomb = matrix[x][y]

    if curr_bomb <= 0:
        continue

    matrix[x][y] = 0
    if x - 1 in range(size) and y - 1 in range(size):
        if matrix[x - 1][y - 1] > 0:
            matrix[x - 1][y - 1] -= curr_bomb
    if x - 1 in range(size) and y in range(size):
        if matrix[x - 1][y] > 0:
            matrix[x - 1][y] -= curr_bomb
    if x - 1 in range(size) and y + 1 in range(size):
        if matrix[x - 1][y + 1] > 0:
            matrix[x - 1][y + 1] -= curr_bomb
    if x in range(size) and y - 1 in range(size):
        if matrix[x][y - 1] > 0:
            matrix[x][y - 1] -= curr_bomb
    if x in range(size) and y + 1 in range(size):
        if matrix[x][y + 1] > 0:
            matrix[x][y + 1] -= curr_bomb
    if x + 1 in range(size) and y - 1 in range(size):
        if matrix[x + 1][y - 1] > 0:
            matrix[x + 1][y - 1] -= curr_bomb
    if x + 1 in range(size) and y in range(size):
        if matrix[x + 1][y] > 0:
            matrix[x + 1][y] -= curr_bomb
    if x + 1 in range(size) and y + 1 in range(size):
        if matrix[x + 1][y + 1] > 0:
            matrix[x + 1][y + 1] -= curr_bomb

alive_cells = 0
sum_alive_cells = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            alive_cells += 1
            sum_alive_cells += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")

for r in range(size):
    for c in range(size):
        print(matrix[r][c], end=" ")
    print()

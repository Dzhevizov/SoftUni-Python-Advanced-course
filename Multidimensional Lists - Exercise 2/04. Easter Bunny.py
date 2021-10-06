import sys

size = int(input())

matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "B":
            bunny_row = i
            bunny_col = j

max_eggs = -sys.maxsize
max_path = []
max_direction = None

directions = ["right", "left", "up", "down"]

for direction in directions:
    eggs = 0
    path = []
    if direction == "right":
        x = 1
        while bunny_col + x < size:
            if matrix[bunny_row][bunny_col + x] == "X":
                break
            eggs += int(matrix[bunny_row][bunny_col + x])
            path.append([bunny_row, bunny_col + x])
            x += 1

    elif direction == "left":
        x = 1
        while bunny_col - x >= 0:
            if matrix[bunny_row][bunny_col - x] == "X":
                break
            eggs += int(matrix[bunny_row][bunny_col - x])
            path.append([bunny_row, bunny_col - x])
            x += 1

    elif direction == "up":
        x = 1
        while bunny_row - x >= 0:
            if matrix[bunny_row - x][bunny_col] == "X":
                break
            eggs += int(matrix[bunny_row - x][bunny_col])
            path.append([bunny_row - x, bunny_col])
            x += 1

    elif direction == "down":
        x = 1
        while bunny_row + x < size:
            if matrix[bunny_row + x][bunny_col] == "X":
                break
            eggs += int(matrix[bunny_row + x][bunny_col])
            path.append([bunny_row + x, bunny_col])
            x += 1

    if eggs > max_eggs:
        max_eggs = eggs
        max_path = path
        max_direction = direction

print(max_direction)
for el in max_path:
    print(el)
print(max_eggs)

from collections import deque

size = int(input())

moves = deque(input().split())

matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

coal_count = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            curr_row = r
            curr_col = c

        if matrix[r][c] == "c":
            coal_count += 1

collected_coal = 0
exited = False

while moves:
    curr_move = moves.popleft()
    if curr_move == "up":
        if curr_row - 1 >= 0:
            curr_row -= 1
    elif curr_move == "down":
        if curr_row + 1 < size:
            curr_row += 1
    elif curr_move == "left":
        if curr_col - 1 >= 0:
            curr_col -= 1
    elif curr_move == "right":
        if curr_col + 1 < size:
            curr_col += 1

    if matrix[curr_row][curr_col] == "c":
        collected_coal += 1
        matrix[curr_row][curr_col] = "*"
        if collected_coal == coal_count:
            print(f"You collected all coal! ({curr_row}, {curr_col})")
            exited = True
            break

    if matrix[curr_row][curr_col] == "e":
        print(f"Game over! ({curr_row}, {curr_col})")
        exited = True
        break

if not exited:
    print(f"{coal_count - collected_coal} pieces of coal left. ({curr_row}, {curr_col})")

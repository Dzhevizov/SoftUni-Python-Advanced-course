from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    line = list(input())
    matrix.append(line)

moves = deque(input())

bunnies = deque()

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "P":
            player_row = r
            player_col = c
        if matrix[r][c] == "B":
            bunny_row = r
            bunny_col = c
            bunnies.append((bunny_row, bunny_col))

won = False
dead = False

while True:
    if moves:
        curr_move = moves.popleft()
    matrix[player_row][player_col] = "."

    if curr_move == "U":
        if player_row - 1 >= 0:
            player_row -= 1
        else:
            won = True
    elif curr_move == "D":
        if player_row + 1 < rows:
            player_row += 1
        else:
            won = True
    elif curr_move == "L":
        if player_col - 1 >= 0:
            player_col -= 1
        else:
            won = True
    elif curr_move == "R":
        if player_col + 1 < cols:
            player_col += 1
        else:
            won = True

    if matrix[player_row][player_col] == "B":
        dead = True

    if matrix[player_row][player_col] == ".":
        matrix[player_row][player_col] = "P"

    next_bunnies = deque()

    for bunny in bunnies:
        if bunny[1] - 1 >= 0:
            if matrix[bunny[0]][bunny[1] - 1] == ".":
                matrix[bunny[0]][bunny[1] - 1] = "B"
                next_bunnies.append((bunny[0], bunny[1] - 1))
            elif matrix[bunny[0]][bunny[1] - 1] == "P":
                matrix[bunny[0]][bunny[1] - 1] = "B"
                dead = True
        if bunny[1] + 1 < cols:
            if matrix[bunny[0]][bunny[1] + 1] == ".":
                matrix[bunny[0]][bunny[1] + 1] = "B"
                next_bunnies.append((bunny[0], bunny[1] + 1))
            elif matrix[bunny[0]][bunny[1] + 1] == "P":
                matrix[bunny[0]][bunny[1] + 1] = "B"
                dead = True
        if bunny[0] - 1 >= 0:
            if matrix[bunny[0] - 1][bunny[1]] == ".":
                matrix[bunny[0] - 1][bunny[1]] = "B"
                next_bunnies.append((bunny[0] - 1, bunny[1]))
            elif matrix[bunny[0] - 1][bunny[1]] == "P":
                matrix[bunny[0] - 1][bunny[1]] = "B"
                dead = True
        if bunny[0] + 1 < rows:
            if matrix[bunny[0] + 1][bunny[1]] == ".":
                matrix[bunny[0] + 1][bunny[1]] = "B"
                next_bunnies.append((bunny[0] + 1, bunny[1]))
            elif matrix[bunny[0] + 1][bunny[1]] == "P":
                matrix[bunny[0] + 1][bunny[1]] = "B"
                dead = True

    bunnies = next_bunnies

    if won:

        if not matrix[player_row][player_col] == "B":
            matrix[player_row][player_col] = "."

        for x in range(rows):
            for y in range(cols):
                print(matrix[x][y], end="")
            print()

        print(f"won: {player_row} {player_col}")
        break

    if dead:
        for x in range(rows):
            for y in range(cols):
                print(matrix[x][y], end="")
            print()

        print(f"dead: {player_row} {player_col}")
        break

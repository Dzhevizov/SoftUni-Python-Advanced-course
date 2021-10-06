size = 5

matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

targets_count = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "A":
            player_row = i
            player_col = j
        elif matrix[i][j] == "x":
            targets_count += 1

commands_count = int(input())
hit_targets = []

for _ in range(commands_count):
    command_data = input().split()
    command = command_data[0]

    if command == "move":
        direction = command_data[1]
        steps = int(command_data[2])

        if direction == "up":
            if player_row - steps >= 0 and matrix[player_row - steps][player_col] == ".":
                matrix[player_row][player_col] = "."
                player_row -= steps
        elif direction == "down":
            if player_row + steps < size and matrix[player_row + steps][player_col] == ".":
                matrix[player_row][player_col] = "."
                player_row += steps
        elif direction == "left":
            if player_col - steps >= 0 and matrix[player_row][player_col - steps] == ".":
                matrix[player_row][player_col] = "."
                player_col -= steps
        elif direction == "right":
            if player_col + steps < size and matrix[player_row][player_col + steps] == ".":
                matrix[player_row][player_col] = "."
                player_col += steps

    elif command == "shoot":
        direction = command_data[1]

        if direction == "up":
            x = 1
            while player_row - x >= 0:
                if matrix[player_row - x][player_col] == "x":
                    matrix[player_row - x][player_col] = "."
                    hit_targets.append([player_row - x, player_col])
                    targets_count -= 1
                    break
                x += 1
        elif direction == "down":
            x = 1
            while player_row + x < size:
                if matrix[player_row + x][player_col] == "x":
                    matrix[player_row + x][player_col] = "."
                    hit_targets.append([player_row + x, player_col])
                    targets_count -= 1
                    break
                x += 1
        elif direction == "left":
            x = 1
            while player_col - x >= 0:
                if matrix[player_row][player_col - x] == "x":
                    matrix[player_row][player_col - x] = "."
                    hit_targets.append([player_row, player_col - x])
                    targets_count -= 1
                    break
                x += 1
        elif direction == "right":
            x = 1
            while player_col + x < size:
                if matrix[player_row][player_col + x] == "x":
                    matrix[player_row][player_col + x] = "."
                    hit_targets.append([player_row, player_col + x])
                    targets_count -= 1
                    break
                x += 1

    if not targets_count:
        break

if not targets_count:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets_count} targets left.")

for el in hit_targets:
    print(el)

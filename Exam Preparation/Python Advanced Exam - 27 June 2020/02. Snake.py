def init_matrix(size):
    matrix = []
    b_rows = []
    b_cols = []
    s_row = 0
    s_col = 0
    for i in range(size):
        line = list(input())
        matrix.append(line)
        if "S" in line:
            s_row = i
            s_col = line.index("S")
        if "B" in line:
            b_rows.append(i)
            b_cols.append(line.index("B"))
    return matrix, s_row, s_col, b_rows, b_cols


def get_next_position(r, c, cmd):
    if cmd == "left":
        c -= 1
    elif cmd == "right":
        c += 1
    elif cmd == "up":
        r -= 1
    elif cmd == "down":
        r += 1
    return r, c


def valid_indexes(r, c, size):
    return 0 <= r < size and 0 <= c < size


matrix_size = int(input())
field, snake_row, snake_col, burrow_rows, burrow_cols = init_matrix(matrix_size)
if len(burrow_rows) == 2 and len(burrow_cols) == 2:
    burrow1 = [burrow_rows[0], burrow_cols[0]]
    burrow2 = [burrow_rows[1], burrow_cols[1]]
total_food = 0

while True:

    if total_food == 10:
        print("You won! You fed the snake.")
        break

    command = input()

    next_row, next_col = get_next_position(snake_row, snake_col, command)

    if not valid_indexes(next_row, next_col, matrix_size):
        field[snake_row][snake_col] = "."
        print("Game over!")
        break

    field[snake_row][snake_col] = "."

    if field[next_row][next_col] == "*":
        total_food += 1
        snake_row, snake_col = next_row, next_col
        field[snake_row][snake_col] = "S"
    elif field[next_row][next_col] == "B":
        field[next_row][next_col] = "."
        if [next_row, next_col] == burrow1:
            snake_row = burrow2[0]
            snake_col = burrow2[1]
        else:
            snake_row = burrow1[0]
            snake_col = burrow1[1]
        field[snake_row][snake_col] = "S"
    elif field[next_row][next_col] == "-":
        snake_row, snake_col = next_row, next_col
        field[snake_row][snake_col] = "S"

print(f"Food eaten: {total_food}")
for line in field:
    print("".join(line))

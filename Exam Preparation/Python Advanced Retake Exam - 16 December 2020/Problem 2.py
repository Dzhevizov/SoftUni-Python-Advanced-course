def init_matrix(size):
    result = []
    for i in range(size):
        line = list(input())
        result.append(line)
        if "P" in line:
            r = i
            c = line.index("P")
    return result, r, c


def get_next_position(row, col, cmd):
    if cmd == "left":
        col -= 1
    elif cmd == "right":
        col += 1
    elif cmd == "up":
        row -= 1
    elif cmd == "down":
        row += 1
    return row, col


def index_validator(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def make_movement(num, row, col, mtx, string):
    for _ in range(num):
        move = input()
        next_row, next_col = get_next_position(row, col, move)
        if index_validator(next_row, next_col, len(mtx)):
            mtx[row][col] = "-"
            row, col = next_row, next_col
            if mtx[row][col].isalpha():
                string += mtx[row][col]
            mtx[row][col] = "P"
        else:
            if string:
                string = string[:-1]
    return mtx, string


init_string = input()
matrix_size = int(input())
matrix, player_row, player_col = init_matrix(matrix_size)
move_num = int(input())
matrix, init_string = make_movement(move_num, player_row, player_col, matrix, init_string)

print(init_string)
for line in matrix:
    print("".join(line))

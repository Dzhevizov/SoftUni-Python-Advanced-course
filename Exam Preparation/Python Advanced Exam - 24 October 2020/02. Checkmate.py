def init_board(num):
    matrix = []
    for i in range(num):
        line = input().split()
        matrix.append(line)
        if "K" in line:
            r = i
            c = line.index("K")
    return matrix, r, c


def check_left(matrix, r, c, num):
    while c > 0:
        if matrix[r][c - 1] == "Q":
            print(f"[{r}, {c - 1}]")
            num += 1
            break
        c -= 1
    return num


def check_right(matrix, r, c, num):
    while c < len(matrix) - 1:
        if matrix[r][c + 1] == "Q":
            print(f"[{r}, {c + 1}]")
            num += 1
            break
        c += 1
    return num


def check_up(matrix, r, c, num):
    while r > 0:
        if matrix[r - 1][c] == "Q":
            print(f"[{r - 1}, {c}]")
            num += 1
            break
        r -= 1
    return num


def check_down(matrix, r, c, num):
    while r < len(matrix) - 1:
        if matrix[r + 1][c] == "Q":
            print(f"[{r + 1}, {c}]")
            num += 1
            break
        r += 1
    return num


def check_up_left(matrix, r, c, num):
    while r > 0 and c > 0:
        if matrix[r - 1][c - 1] == "Q":
            print(f"[{r - 1}, {c - 1}]")
            num += 1
            break
        r -= 1
        c -= 1
    return num


def check_down_right(matrix, r, c, num):
    while r < len(matrix) - 1 and c < len(matrix) - 1:
        if matrix[r + 1][c + 1] == "Q":
            print(f"[{r + 1}, {c + 1}]")
            num += 1
            break
        r += 1
        c += 1
    return num


def check_up_right(matrix, r, c, num):
    while r > 0 and c < len(matrix) - 1:
        if matrix[r - 1][c + 1] == "Q":
            print(f"[{r - 1}, {c + 1}]")
            num += 1
            break
        r -= 1
        c += 1
    return num


def check_down_left(matrix, r, c, num):
    while r < len(matrix) - 1 and c > 0:
        if matrix[r + 1][c - 1] == "Q":
            print(f"[{r + 1}, {c - 1}]")
            num += 1
            break
        r += 1
        c -= 1
    return num


size_of_board = 8
chess_board, king_row, king_col = init_board(size_of_board)
count = 0

count = check_left(chess_board, king_row, king_col, count)
count = check_right(chess_board, king_row, king_col, count)
count = check_up(chess_board, king_row, king_col, count)
count = check_down(chess_board, king_row, king_col, count)
count = check_up_left(chess_board, king_row, king_col, count)
count = check_down_right(chess_board, king_row, king_col, count)
count = check_up_right(chess_board, king_row, king_col, count)
count = check_down_left(chess_board, king_row, king_col, count)
if count == 0:
    print("The king is safe!")

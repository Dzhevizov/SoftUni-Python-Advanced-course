def init_matrix(size):
    matrix = []
    for _ in range(size):
        line = input().split()
        matrix.append(line)
    return matrix


def valid_indexes(row, column, size):
    return 0 <= row < size and 0 <= column < size


def take_column_sum(col, matrix):
    result = 0
    for r in range(len(matrix)):
        if matrix[r][col].isdigit():
            result += int(matrix[r][col])
    return result


board_size = 6
board = init_matrix(board_size)
score = 0
throws_num = 3
prize = None
needed_points = 0

for _ in range(throws_num):
    curr_row, curr_col = map(int, input()[1:-1].split(", "))

    if not valid_indexes(curr_row, curr_col, board_size):
        continue

    if board[curr_row][curr_col] == "B":
        score += take_column_sum(curr_col, board)
        board[curr_row][curr_col] = "0"

if 100 <= score < 200:
    prize = "Football"
elif 200 <= score < 300:
    prize = "Teddy Bear"
elif score >= 300:
    prize = "Lego Construction Set"
else:
    needed_points = 100 - score

if prize:
    print(f"Good job! You scored {score} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {needed_points} points more to win a prize.")

def init_matrix(size):
    matrix = []
    for _ in range(size):
        line = [0 for _ in range(size)]
        matrix.append(line)
    return matrix


def place_bombs(matrix, bombs):
    for _ in range(bombs):
        row, col = map(int, input()[1:-1].split(", "))
        matrix[row][col] = "*"
    return matrix


def count_bombs(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            counter = 0
            if not matrix[row][col] == 0:
                continue
            if row - 1 >= 0 and col - 1 >= 0:
                if matrix[row - 1][col - 1] == "*":
                    counter += 1
            if row - 1 >= 0 and col + 1 < len(matrix):
                if matrix[row - 1][col + 1] == "*":
                    counter += 1
            if row - 1 >= 0:
                if matrix[row - 1][col] == "*":
                    counter += 1
            if row + 1 < len(matrix) and col - 1 >= 0:
                if matrix[row + 1][col - 1] == "*":
                    counter += 1
            if row + 1 < len(matrix) and col + 1 < len(matrix):
                if matrix[row + 1][col + 1] == "*":
                    counter += 1
            if row + 1 < len(matrix):
                if matrix[row + 1][col] == "*":
                    counter += 1
            if col - 1 >= 0:
                if matrix[row][col - 1] == "*":
                    counter += 1
            if col + 1 < len(matrix):
                if matrix[row][col + 1] == "*":
                    counter += 1
            matrix[row][col] = counter
    return matrix


matrix_size = int(input())
num_of_bombs = int(input())
field = init_matrix(matrix_size)
field = place_bombs(field, num_of_bombs)
field = count_bombs(field)
for line in field:
    print(" ".join(map(str, line)))

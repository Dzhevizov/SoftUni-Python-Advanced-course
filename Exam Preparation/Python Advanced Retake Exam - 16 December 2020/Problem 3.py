def get_magic_triangle(num):
    matrix = [[1], [1, 1]]
    for row in range(2, num):
        matrix.append([None for _ in range(row + 1)])
        for col in range(row + 1):
            if col == 0:
                matrix[row][col] = 1
            elif col == row:
                matrix[row][col] = 1
            else:
                matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
    return matrix


print(get_magic_triangle(5))

presents_count = int(input())
size = int(input())
matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

nice_kids_count = 0
gifted_nice_kids = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "S":
            santa_row = i
            santa_col = j
        elif matrix[i][j] == "V":
            nice_kids_count += 1

command = input()

while not command == "Christmas morning":

    matrix[santa_row][santa_col] = "-"

    if command == "up":
        santa_row -= 1
    elif command == "down":
        santa_row += 1
    elif command == "left":
        santa_col -= 1
    elif command == "right":
        santa_col += 1

    if matrix[santa_row][santa_col] == "V":
        presents_count -= 1
        gifted_nice_kids += 1
    elif matrix[santa_row][santa_col] == "C":
        if matrix[santa_row - 1][santa_col] == "V":
            matrix[santa_row - 1][santa_col] = "-"
            presents_count -= 1
            gifted_nice_kids += 1
        elif matrix[santa_row - 1][santa_col] == "X":
            matrix[santa_row - 1][santa_col] = "-"
            presents_count -= 1
        if matrix[santa_row + 1][santa_col] == "V":
            matrix[santa_row + 1][santa_col] = "-"
            presents_count -= 1
            gifted_nice_kids += 1
        elif matrix[santa_row + 1][santa_col] == "X":
            matrix[santa_row + 1][santa_col] = "-"
            presents_count -= 1
        if matrix[santa_row][santa_col - 1] == "V":
            matrix[santa_row][santa_col - 1] = "-"
            presents_count -= 1
            gifted_nice_kids += 1
        elif matrix[santa_row][santa_col - 1] == "X":
            matrix[santa_row][santa_col - 1] = "-"
            presents_count -= 1
        if matrix[santa_row][santa_col + 1] == "V":
            matrix[santa_row][santa_col + 1] = "-"
            presents_count -= 1
            gifted_nice_kids += 1
        elif matrix[santa_row][santa_col + 1] == "X":
            matrix[santa_row][santa_col - 1] = "-"
            presents_count -= 1

    matrix[santa_row][santa_col] = "S"

    if not presents_count:
        break

    command = input()

if not presents_count and not gifted_nice_kids == nice_kids_count:
    print("Santa ran out of presents!")

for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=" ")
    print()

if gifted_nice_kids == nice_kids_count:
    print(f"Good job, Santa! {gifted_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count - gifted_nice_kids} nice kid/s.")

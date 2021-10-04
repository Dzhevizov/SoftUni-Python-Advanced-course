rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    line = input().split()
    matrix.append(line)

command_args = input()

while not command_args == "END":
    command_args = command_args.split()
    if command_args[0] == "swap" and len(command_args) == 5:
        row1, col1, row2, col2 = map(int, command_args[1:])
    else:
        print("Invalid input!")
        command_args = input()
        continue

    if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for x in range(rows):
            for y in range(cols):
                print(matrix[x][y], end=" ")
            print()
    else:
        print("Invalid input!")

    command_args = input()

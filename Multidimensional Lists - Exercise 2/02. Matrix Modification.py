rows = int(input())

matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

command_data = input()

while not command_data == "END":

    command, row, col, value = command_data.split()

    if command == "Add":
        if 0 <= int(row) < rows and 0 <= int(col) < len(matrix[int(row)]):
            matrix[int(row)][int(col)] += int(value)
        else:
            print("Invalid coordinates")
    elif command == "Subtract":
        if 0 <= int(row) < rows and 0 <= int(col) < len(matrix[int(row)]):
            matrix[int(row)][int(col)] -= int(value)
        else:
            print("Invalid coordinates")

    command_data = input()

for x in matrix:
    for y in x:
        print(y, end=" ")
    print()

size = int(input())

matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "A":
            alice_row = i
            alice_col = j
        elif matrix[i][j] == "R":
            rabbit_row = i
            rabbit_col = j

tea_bags = 0

while tea_bags < 10:
    command = input()
    matrix[alice_row][alice_col] = "*"
    if command == "up":
        if alice_row - 1 >= 0:
            alice_row -= 1
            if matrix[alice_row][alice_col] == "R":
                matrix[alice_row][alice_col] = "*"
                break
            elif matrix[alice_row][alice_col].isdigit():
                tea_bags += int(matrix[alice_row][alice_col])
                matrix[alice_row][alice_col] = "*"
        else:
            break
    elif command == "down":
        if alice_row + 1 < size:
            alice_row += 1
            if matrix[alice_row][alice_col] == "R":
                matrix[alice_row][alice_col] = "*"
                break
            elif matrix[alice_row][alice_col].isdigit():
                tea_bags += int(matrix[alice_row][alice_col])
                matrix[alice_row][alice_col] = "*"
        else:
            break
    elif command == "left":
        if alice_col - 1 >= 0:
            alice_col -= 1
            if matrix[alice_row][alice_col] == "R":
                matrix[alice_row][alice_col] = "*"
                break
            elif matrix[alice_row][alice_col].isdigit():
                tea_bags += int(matrix[alice_row][alice_col])
                matrix[alice_row][alice_col] = "*"
        else:
            break
    elif command == "right":
        if alice_col + 1 < size:
            alice_col += 1
            if matrix[alice_row][alice_col] == "R":
                matrix[alice_row][alice_col] = "*"
                break
            elif matrix[alice_row][alice_col].isdigit():
                tea_bags += int(matrix[alice_row][alice_col])
                matrix[alice_row][alice_col] = "*"
        else:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=" ")
    print()

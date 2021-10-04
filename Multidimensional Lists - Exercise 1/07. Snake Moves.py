rows, cols = [int(x) for x in input().split()]

snake = input()

index = 0

matrix = [[None for c in range(cols)] for r in range(rows)]

for r in range(rows):
    for c in range(cols):
        if r % 2 == 0:
            matrix[r][c] = snake[index]
        else:
            matrix[r][cols - 1 - c] = snake[index]
        index += 1
        if index == len(snake):
            index = 0

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end="")
    print()

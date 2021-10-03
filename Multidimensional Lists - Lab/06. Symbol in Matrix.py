size = int(input())

matrix = []

for _ in range(size):
    line = list(input())
    matrix.append(line)

symbol = input()
is_found = False

for i in range(size):
    for j in range(size):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{symbol} does not occur in the matrix")

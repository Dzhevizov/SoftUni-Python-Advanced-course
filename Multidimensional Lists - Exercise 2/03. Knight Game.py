size = int(input())

matrix = []

for _ in range(size):
    line = list(input())
    matrix.append(line)

removed_knights = 0

while True:
    max_hits = 0
    max_knight = ()
    for i in range(size):
        for j in range(size):
            hits = 0
            if matrix[i][j] == "K":
                if i - 2 >= 0 and j - 1 >= 0 and matrix[i - 2][j - 1] == "K":
                    hits += 1
                if i - 2 >= 0 and j + 1 < size and matrix[i - 2][j + 1] == "K":
                    hits += 1
                if i - 1 >= 0 and j - 2 >= 0 and matrix[i - 1][j - 2] == "K":
                    hits += 1
                if i - 1 >= 0 and j + 2 < size and matrix[i - 1][j + 2] == "K":
                    hits += 1
                if i + 1 < size and j - 2 >= 0 and matrix[i + 1][j - 2] == "K":
                    hits += 1
                if i + 1 < size and j + 2 < size and matrix[i + 1][j + 2] == "K":
                    hits += 1
                if i + 2 < size and j - 1 >=0 and matrix[i + 2][j - 1] == "K":
                    hits += 1
                if i + 2 < size and j + 1 < size and matrix[i + 2][j + 1] == "K":
                    hits += 1

                if hits > max_hits:
                    max_hits = hits
                    max_knight = (i, j)

    if max_hits > 0:
        matrix[max_knight[0]][max_knight[1]] = '0'
        removed_knights += 1
    else:
        print(removed_knights)
        break

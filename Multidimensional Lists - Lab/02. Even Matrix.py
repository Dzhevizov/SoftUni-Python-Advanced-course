rows = int(input())

given_matrix = []

for i in range(rows):
    line = [int(x) for x in input().split(", ")]
    given_matrix.append(line)

even_matrix = [[j for j in i if j % 2 == 0] for i in given_matrix]

print(even_matrix)

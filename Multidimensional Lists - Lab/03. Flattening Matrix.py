rows = int(input())

given_matrix = []

for i in range(rows):
    line = [int(x) for x in input().split(", ")]
    given_matrix.append(line)

flattened_matrix = [j for i in given_matrix for j in i]

print(flattened_matrix)

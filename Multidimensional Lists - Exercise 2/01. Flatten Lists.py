lists = input().strip().split("|")
matrix = []

for el in lists:
    nums = el.strip().split()
    matrix.append(nums)

for r in reversed(matrix):
    for el in r:
        print(el, end=" ")

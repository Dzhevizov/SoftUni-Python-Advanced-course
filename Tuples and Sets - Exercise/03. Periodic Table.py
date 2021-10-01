num_of_lines = int(input())

unique_elements = set()

for _ in range(num_of_lines):
    line = input().split()
    for el in line:
        unique_elements.add(el)

for el in unique_elements:
    print(el)

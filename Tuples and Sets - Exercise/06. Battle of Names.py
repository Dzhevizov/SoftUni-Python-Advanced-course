num_of_lines = int(input())

odd_set = set()
even_set = set()

for i in range(1, num_of_lines + 1):
    name = input()
    sum_name = 0

    for ch in name:
        sum_name += ord(ch)

    result = sum_name // i

    if result % 2:
        odd_set.add(result)
    else:
        even_set.add(result)

if sum(odd_set) == sum(even_set):
    print(", ".join(map(str, odd_set.union(even_set))))
elif sum(odd_set) > sum(even_set):
    print(", ".join(map(str, odd_set.difference(even_set))))
else:
    print(", ".join(map(str, odd_set.symmetric_difference(even_set))))

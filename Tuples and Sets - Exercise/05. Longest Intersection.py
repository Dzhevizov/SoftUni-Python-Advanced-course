num_of_lines = int(input())

longest_intersection = set()

for _ in range(num_of_lines):
    first_range, second_range = input().split("-")
    first_start, first_end = map(int, first_range.split(","))
    second_start, second_end = map(int, second_range.split(","))
    first_set = set()
    second_set = set()
    for el in range(first_start, first_end + 1):
        first_set.add(el)
    for el in range(second_start, second_end + 1):
        second_set.add(el)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_intersection_numbers = ", ".join(map(str, longest_intersection))
print(f"Longest intersection is [{longest_intersection_numbers}] with length {len(longest_intersection)}")

from collections import deque

text = deque(input().split())

main_colors = ["red", "yellow", "blue"]

secondary_colors = ["orange", "purple", "green"]

secondary_colors_conditions = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

collected_colors = []

while text:
    first = text.popleft()
    if text:
        second = text.pop()
    else:
        second = ""

    result1 = first + second
    result2 = second + first

    if result1 in main_colors or result1 in secondary_colors:
        collected_colors.append(result1)
    elif result2 in main_colors or result2 in secondary_colors:
        collected_colors.append(result2)
    else:
        first1 = first[:-1]
        if first1:
            text.insert(len(text) // 2, first1)
        if second:
            second1 = second[:-1]
            if second1:
                text.insert(len(text) // 2, second1)

for el in collected_colors:
    if el in secondary_colors:
        if secondary_colors_conditions[el][0] in collected_colors and \
                secondary_colors_conditions[el][1] in collected_colors:
            continue
        else:
            collected_colors.remove(el)

print(collected_colors)

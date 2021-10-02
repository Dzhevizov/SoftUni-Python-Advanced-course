from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees and nectar:

    curr_bee = bees[0]
    curr_nectar = nectar[-1]

    if curr_bee <= curr_nectar:
        if symbols:
            curr_symbol = symbols.popleft()
        else:
            break

        if curr_symbol == "+":
            total_honey += abs(curr_bee + curr_nectar)
        elif curr_symbol == "-":
            total_honey += abs(curr_bee - curr_nectar)
        elif curr_symbol == "*":
            total_honey += abs(curr_bee * curr_nectar)
        elif curr_symbol == "/":
            if curr_nectar:
                total_honey += abs(curr_bee / curr_nectar)

        bees.popleft()
        nectar.pop()

    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")

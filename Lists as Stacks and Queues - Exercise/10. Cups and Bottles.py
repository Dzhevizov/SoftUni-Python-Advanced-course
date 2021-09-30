from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:

    curr_cup = cups.popleft()
    curr_bottle = bottles.pop()

    if curr_cup <= curr_bottle:
        wasted_water += curr_bottle - curr_cup
    else:
        curr_cup -= curr_bottle
        cups.appendleft(curr_cup)

if not cups:
    print(f"Bottles: ", end="")
    while bottles:
        print(f"{bottles.pop()}", end=" ")
else:
    print(f"Cups: ", end="")
    while cups:
        print(f"{cups.popleft()}", end=" ")
print(f"\nWasted litters of water: {wasted_water}")

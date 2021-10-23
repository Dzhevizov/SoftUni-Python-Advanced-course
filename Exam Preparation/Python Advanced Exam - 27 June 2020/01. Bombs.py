from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]

bomb_types = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0]
}

succeeded = False

while True:

    if bomb_types["Datura Bombs"][1] >= 3 and \
            bomb_types["Cherry Bombs"][1] >= 3 and \
            bomb_types["Smoke Decoy Bombs"][1] >= 3:
        succeeded = True
        break

    if not bomb_effects or not bomb_casings:
        break

    curr_effect = bomb_effects.popleft()
    curr_casing = bomb_casings.pop()

    materials_sum = curr_effect + curr_casing

    if materials_sum == bomb_types["Datura Bombs"][0]:
        bomb_types["Datura Bombs"][1] += 1
    elif materials_sum == bomb_types["Cherry Bombs"][0]:
        bomb_types["Cherry Bombs"][1] += 1
    elif materials_sum == bomb_types["Smoke Decoy Bombs"][0]:
        bomb_types["Smoke Decoy Bombs"][1] += 1
    else:
        curr_casing -= 5
        bomb_effects.appendleft(curr_effect)
        bomb_casings.append(curr_casing)

if succeeded:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for bombs, values in sorted(bomb_types.items()):
    print(f"{bombs}: {values[1]}")

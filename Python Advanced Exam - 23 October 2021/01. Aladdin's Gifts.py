from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

succeed = False

while True:

    if gifts["Gemstone"] >= 1 and gifts["Porcelain Sculpture"] >= 1:
        succeed = True

    if gifts["Gold"] >= 1 and gifts["Diamond Jewellery"] >= 1:
        succeed = True

    if not materials or not magic_levels:
        break

    curr_material = materials.pop()
    curr_magic_level = magic_levels.popleft()

    mix = curr_material + curr_magic_level

    if mix < 100 and mix % 2 == 0:
        curr_material *= 2
        curr_magic_level *= 3
        mix = curr_material + curr_magic_level
    elif mix < 100 and not mix % 2 == 0:
        mix *= 2
    elif mix >= 500:
        mix /= 2

    if 100 <= mix < 200:
        gifts["Gemstone"] += 1
    elif 200 <= mix < 300:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= mix < 400:
        gifts["Gold"] += 1
    elif 400 <= mix < 500:
        gifts["Diamond Jewellery"] += 1

if succeed:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for gift in sorted(gifts):
    if gifts[gift] > 0:
        print(f"{gift}: {gifts[gift]}")

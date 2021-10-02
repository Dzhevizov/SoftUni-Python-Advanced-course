from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

needed_magic = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}
is_done = False

crafted_presents = {}

while materials and magic:

    curr_material = materials[-1]
    curr_magic = magic[0]

    if not curr_material and not curr_magic:
        materials.pop()
        magic.popleft()
        continue

    if not curr_material:
        materials.pop()
        continue

    if not curr_magic:
        magic.popleft()
        continue

    total_magic = curr_material * curr_magic

    if total_magic < 0:
        result = curr_material + curr_magic
        materials.pop()
        magic.popleft()
        materials.append(result)
    else:
        if total_magic == needed_magic["Doll"]:
            if "Doll" not in crafted_presents:
                crafted_presents["Doll"] = 0
            crafted_presents["Doll"] += 1
            materials.pop()
            magic.popleft()
        elif total_magic == needed_magic["Wooden train"]:
            if "Wooden train" not in crafted_presents:
                crafted_presents["Wooden train"] = 0
            crafted_presents["Wooden train"] += 1
            materials.pop()
            magic.popleft()
        elif total_magic == needed_magic["Teddy bear"]:
            if "Teddy bear" not in crafted_presents:
                crafted_presents["Teddy bear"] = 0
            crafted_presents["Teddy bear"] += 1
            materials.pop()
            magic.popleft()
        elif total_magic == needed_magic["Bicycle"]:
            if "Bicycle" not in crafted_presents:
                crafted_presents["Bicycle"] = 0
            crafted_presents["Bicycle"] += 1
            materials.pop()
            magic.popleft()
        else:
            magic.popleft()
            materials[-1] += 15

if "Doll" in crafted_presents and "Wooden train" in crafted_presents:
    is_done = True
elif "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents:
    is_done = True

if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for present, amount in sorted(crafted_presents.items()):
    print(f"{present}: {amount}")

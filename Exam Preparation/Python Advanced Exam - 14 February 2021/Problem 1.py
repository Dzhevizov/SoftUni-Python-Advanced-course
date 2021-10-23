from collections import deque

is_succeeded = False

firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while True:

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        is_succeeded = True
        break

    if not firework_effects or not explosive_power:
        break

    curr_effect = firework_effects.popleft()
    curr_power = explosive_power.pop()

    if curr_effect <= 0:
        explosive_power.append(curr_power)
        continue

    if curr_power <= 0:
        firework_effects.appendleft(curr_effect)
        continue

    sum_elements = curr_effect + curr_power

    if sum_elements % 15 == 0:
        crossette_firework += 1
    elif sum_elements % 3 == 0:
        palm_firework += 1
    elif sum_elements % 5 == 0:
        willow_firework += 1
    else:
        curr_effect -= 1
        firework_effects.append(curr_effect)
        explosive_power.append(curr_power)

if is_succeeded:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")

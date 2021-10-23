from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0

while True:

    if not males or not females:
        break

    curr_male = males.pop()
    curr_female = females.popleft()

    if curr_male <= 0:
        females.appendleft(curr_female)
        continue

    if curr_female <= 0:
        males.append(curr_male)
        continue

    if curr_male % 25 == 0:
        if males:
            males.pop()
        females.appendleft(curr_female)
        continue

    if curr_female % 25 == 0:
        if females:
            females.popleft()
        males.append(curr_male)
        continue

    if curr_male == curr_female:
        matches += 1
    else:
        curr_male -= 2
        males.append(curr_male)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")

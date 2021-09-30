from collections import deque
num_of_petrol_pumps = int(input())
petrol_pumps = deque()

for _ in range(num_of_petrol_pumps):
    petrol_pumps.append(list(map(int, input().split())))

for index in range(num_of_petrol_pumps):
    is_completed = True
    curr_fuel = 0
    for pump in petrol_pumps:
        curr_fuel += pump[0]
        distance = pump[1]
        if curr_fuel >= distance:
            curr_fuel -= distance
        else:
            is_completed = False
            break
    if is_completed:
        print(index)
        break
    petrol_pumps.append(petrol_pumps.popleft())

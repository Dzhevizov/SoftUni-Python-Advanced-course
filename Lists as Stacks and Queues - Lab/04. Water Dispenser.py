from collections import deque

water_quantity = int(input())

queue = deque()

names = input()

while not names == "Start":
    queue.appendleft(names)
    names = input()

command = input()

while not command == "End":

    if command.startswith("refill"):
        liters = int(command.split()[1])
        water_quantity += liters
        command = input()
        continue

    liters = int(command)

    if liters <= water_quantity:
        water_quantity -= liters
        print(f"{queue.pop()} got water")
    else:
        print(f"{queue.pop()} must wait")

    command = input()

print(f"{water_quantity} liters left")

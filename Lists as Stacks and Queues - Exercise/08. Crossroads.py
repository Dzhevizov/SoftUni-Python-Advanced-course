from collections import deque

initial_green_light = int(input())
initial_free_window = int(input())

queue = deque()
in_crossroad = None
total_cars = 0
crashed = False

command = input()

while not command == "END":
    if command == "green":
        green_light = initial_green_light
        free_window = initial_free_window
        while green_light:
            if not queue:
                break

            curr_car = queue.popleft()

            for i in range(len(curr_car)):
                in_crossroad = curr_car[i]
                if green_light > 0:
                    green_light -= 1
                else:
                    if free_window > 0:
                        free_window -= 1
                    else:
                        print("A crash happened!")
                        print(f"{curr_car} was hit at {in_crossroad}.")
                        crashed = True
                        break
            if not crashed:
                total_cars += 1

    else:
        queue.append(command)

    if crashed:
        break

    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")

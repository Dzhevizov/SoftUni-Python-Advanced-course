num_of_commands = int(input())

parking_lot = set()

for _ in range(num_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    for number in parking_lot:
        print(number)
else:
    print("Parking Lot is Empty")

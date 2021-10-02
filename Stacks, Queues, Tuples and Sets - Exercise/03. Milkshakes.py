from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0
shakes_made = False
flag = False

while chocolates and cups_of_milk:

    curr_chocolate = chocolates.pop()
    curr_cup_of_milk = cups_of_milk.popleft()

    while curr_chocolate <= 0:
        if chocolates:
            curr_chocolate = chocolates.pop()
        else:
            if curr_cup_of_milk > 0:
                cups_of_milk.appendleft(curr_cup_of_milk)
            flag = True
            break

    while curr_cup_of_milk <= 0:
        if cups_of_milk:
            curr_cup_of_milk = cups_of_milk.popleft()
        else:
            if curr_chocolate > 0:
                chocolates.append(curr_chocolate)
            flag = True
            break

    if flag:
        break

    if curr_chocolate == curr_cup_of_milk:
        milkshakes += 1
    else:
        curr_chocolate -= 5
        chocolates.append(curr_chocolate)
        cups_of_milk.append(curr_cup_of_milk)

    if milkshakes == 5:
        shakes_made = True
        break

if shakes_made:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f'Chocolate: {", ".join(map(str, chocolates))}')
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f'Milk: {", ".join(map(str, cups_of_milk))}')
else:
    print("Milk: empty")

from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    curr_order = orders.popleft()
    if curr_order > food_quantity:
        orders.appendleft(curr_order)
        break
    food_quantity -= curr_order

if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")

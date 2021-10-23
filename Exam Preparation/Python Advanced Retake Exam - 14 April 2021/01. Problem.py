from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees_capacities = [int(x) for x in input().split(", ")]

total_pizzas = 0

while True:

    if not pizza_orders or not employees_capacities:
        break

    curr_order = pizza_orders.popleft()
    curr_employee = employees_capacities.pop()

    if curr_order <= 0 or curr_order > 10:
        employees_capacities.append(curr_employee)
        continue

    if curr_employee >= curr_order:
        total_pizzas += curr_order
    else:
        curr_order -= curr_employee
        total_pizzas += curr_employee
        pizza_orders.appendleft(curr_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employees_capacities:
        print(f"Employees: {', '.join(map(str, employees_capacities))}")

if not employees_capacities and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")

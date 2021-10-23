from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while True:

    if not customers or not taxis:
        break

    curr_customer = customers.popleft()
    curr_taxi = taxis.pop()

    if curr_customer <= curr_taxi:
        total_time += curr_customer
    else:
        customers.appendleft(curr_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")

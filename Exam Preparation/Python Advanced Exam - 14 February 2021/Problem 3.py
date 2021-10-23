from collections import deque


def stock_availability(*args):
    inventory = deque(args[0])
    operation = args[1]
    params = args[2:]

    if operation == "delivery":
        for el in params:
            inventory.append(el)
    elif operation == "sell":
        if len(args) == 2:
            inventory.popleft()
        elif isinstance(args[2], int):
            for _ in range(args[2]):
                inventory.popleft()
        else:
            for el in params:
                inventory = deque(x for x in inventory if not x == el)
    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

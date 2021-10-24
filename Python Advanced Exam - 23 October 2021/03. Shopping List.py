from collections import deque


def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    bought_products = deque()
    for product, values in kwargs.items():
        if len(bought_products) == 5:
            break
        total = values[0] * values[1]
        if total <= budget:
            bought_products.append((product, total))
            budget -= total

    result = []
    while bought_products:
        curr_product = bought_products.popleft()
        result.append(f"You bought {curr_product[0]} for {curr_product[1]:.2f} leva.")
    return "\n".join(result)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

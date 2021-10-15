from math import log


def calculate_logarithm(num, b):
    if b.isdigit():
        return log(num, int(b))
    return log(num)


number = int(input())
base = input()
print(f"{calculate_logarithm(number, base):.2f}")

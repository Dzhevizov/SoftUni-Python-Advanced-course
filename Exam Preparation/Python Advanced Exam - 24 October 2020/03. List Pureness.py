import sys
from collections import deque


def best_list_pureness(*args):
    list_of_nums = deque(args[0])
    rotates = args[1]
    best_pureness = -sys.maxsize
    best_rotation = 0
    for rotation in range(rotates + 1):
        pureness = sum(i * list_of_nums[i] for i in range(len(list_of_nums)))
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        rotated_element = list_of_nums.pop()
        list_of_nums.appendleft(rotated_element)
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


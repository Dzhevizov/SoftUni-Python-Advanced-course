from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    result = kwargs
    while nums:
        curr_element = nums.popleft()
        result['a'] = result['a'] + curr_element
        if nums:
            curr_element = nums.popleft()
            result['s'] = result['s'] - curr_element
        if nums:
            curr_element = nums.popleft()
            if not curr_element == 0:
                result['d'] = result['d'] / curr_element
        if nums:
            curr_element = nums.popleft()
            result['m'] = result['m'] * curr_element

    return result


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))

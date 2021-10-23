from collections import deque


def list_manipulator(*args):
    init_list = deque(args[0])
    command = args[1]
    direction = args[2]
    params = None

    if len(args) >= 4:
        params = deque(args[3:])

    if command == "add" and direction == "beginning":
        while len(params) > 0:
            init_list.appendleft(params.pop())
    elif command == "add" and direction == "end":
        while len(params) > 0:
            init_list.append(params.popleft())
    elif command == "remove" and direction == "beginning":
        if params:
            for _ in range(params[0]):
                init_list.popleft()
        else:
            init_list.popleft()
    elif command == "remove" and direction == "end":
        if params:
            for _ in range(params[0]):
                init_list.pop()
        else:
            init_list.pop()
    return list(init_list)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

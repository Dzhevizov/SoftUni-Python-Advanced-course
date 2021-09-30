stack = []

N = int(input())

for _ in range(N):

    command_data = input().split()
    command = command_data[0]

    if command == "1":
        num = int(command_data[1])
        stack.append(num)

    elif command == "2":
        if stack:
            stack.pop()

    elif command == "3":
        if stack:
            print(max(stack))

    elif command == "4":
        if stack:
            print(min(stack))

while stack:

    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")

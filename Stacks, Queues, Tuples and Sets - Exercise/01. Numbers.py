first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}

num_of_commands = int(input())

for _ in range(num_of_commands):
    command_data = input().split()
    command = command_data[0]

    if command == "Add":
        curr_set = command_data[1]
        numbers = map(int, command_data[2:])

        for num in numbers:
            if curr_set == "First":
                first.add(num)
            else:
                second.add(num)

    elif command == "Remove":
        curr_set = command_data[1]
        numbers = map(int, command_data[2:])

        for num in numbers:
            if curr_set == "First" and num in first:
                first.remove(num)
            elif curr_set == "Second" and num in second:
                second.remove(num)

    elif command == "Check":
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(", ".join(map(str, sorted(first))))
print(", ".join(map(str, sorted(second))))

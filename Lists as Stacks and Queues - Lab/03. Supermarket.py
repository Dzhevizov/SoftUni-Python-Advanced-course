from collections import deque

queue = deque()

command = input()

while not command == "End":

    if command == "Paid":
        while queue:
            print(queue.pop())
    else:
        queue.appendleft(command)

    command = input()

print(f"{len(queue)} people remaining.")

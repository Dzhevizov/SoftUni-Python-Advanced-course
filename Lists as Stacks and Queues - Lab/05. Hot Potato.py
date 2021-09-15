from collections import deque

kids = input().split()
n_toss = int(input())
toss = 0

queue = deque(kids)

while queue:

    if len(queue) == 1:
        print(f"Last is {queue.popleft()}")
        continue

    toss += 1

    if toss == n_toss:
        print(f"Removed {queue.popleft()}")
        toss = 0
        continue

    queue.append(queue.popleft())

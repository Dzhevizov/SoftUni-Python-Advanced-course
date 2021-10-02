from collections import deque

sequence = deque(input().split())

result = int(sequence.popleft())

queue = deque()

while sequence:
    curr_el = sequence.popleft()
    if curr_el == '+':
        while queue:
            result += int(queue.popleft())
    elif curr_el == '-':
        while queue:
            result -= int(queue.popleft())
    elif curr_el == '*':
        while queue:
            result *= int(queue.popleft())
    elif curr_el == '/':
        while queue:
            result //= int(queue.popleft())
    else:
        queue.append(curr_el)

print(result)

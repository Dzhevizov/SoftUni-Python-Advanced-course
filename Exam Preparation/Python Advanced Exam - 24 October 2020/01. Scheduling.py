import sys

jobs = [int(x) for x in input().split(", ")]
index = int(input())

cycles = 0
count = 1

interested_job = jobs[index]

if interested_job in jobs[:index]:
    for el in jobs[:index]:
        if el == interested_job:
            count += 1

while True:

    shortest_job = sys.maxsize
    for el in jobs:
        if el < shortest_job:
            shortest_job = el

    if shortest_job == interested_job:
        cycles += shortest_job * count
        break

    cycles += shortest_job
    jobs.remove(shortest_job)

print(cycles)

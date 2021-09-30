from datetime import datetime, timedelta
from collections import deque

robots_list = input().split(';')
starting_time = datetime.strptime(input(), '%H:%M:%S')

robots = []

for el in robots_list:
    name, process_time = el.split('-')
    robot = {}
    robot['name'] = name
    robot['process_time'] = int(process_time)
    robot['free_at'] = starting_time
    robots.append(robot)

products = deque()

product = input()

while not product == "End":
    products.append(product)
    product = input()

operation = 1

while products:
    time = starting_time + timedelta(seconds=operation)
    robot_found = False
    for robot in robots:
        if robot['free_at'] <= time:
            print(f'{robot["name"]} - {products.popleft()} [{time.strftime("%H:%M:%S")}]')
            robot['free_at'] = time + timedelta(seconds=robot['process_time'])
            robot_found = True
            break
    if products and not robot_found:
        products.append(products.popleft())
    operation += 1

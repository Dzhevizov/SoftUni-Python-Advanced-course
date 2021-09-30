from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

earned_money = 0

bullets_count = barrel_size

while bullets and locks:

    curr_bullet = bullets.pop()
    curr_lock = locks.popleft()

    if curr_bullet <= curr_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(curr_lock)

    bullets_count -= 1
    earned_money -= bullet_price

    if not bullets_count and bullets:
        print("Reloading!")
        bullets_count = barrel_size

if not locks:
    earned_money += intelligence_value
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

def init_matrix(n):
    result = []
    for i in range(n):
        line = input().split()
        result.append(line)
        if "P" in line:
            r = i
            c = line.index("P")
    return result, r, c


def make_move(r, c, cmd):
    if cmd == "left":
        c -= 1
    elif cmd == "right":
        c += 1
    elif cmd == "up":
        r -= 1
    elif cmd == "down":
        r += 1
    return r, c


def valid_index(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


size = int(input())
field, player_row, player_col = init_matrix(size)
coins = 0
path = []
is_winner = False

while True:

    if coins >= 100:
        is_winner = True
        break

    move = input()
    player_row, player_col = make_move(player_row, player_col, move)

    if not valid_index(player_row, player_col, size):
        coins //= 2
        break

    if field[player_row][player_col] == "X":
        coins //= 2
        break

    position = field[player_row][player_col]
    if position.isdigit():
        coins += int(position)
        path.append([player_row, player_col])

if is_winner:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print(f"Your path:")
for el in path:
    print(el)

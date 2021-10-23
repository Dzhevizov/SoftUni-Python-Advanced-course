def init_dartboard(lines):
    result = []
    for i in range(lines):
        line = input().split()
        result.append(line)
    return result


def in_dartboard(index1, index2, size):
    if 0 <= index1 < size and 0 <= index2 < size:
        return True
    return False


def find_sum(r, c, matrix):
    result = int(matrix[r][0]) + int(matrix[r][len(matrix) - 1]) + \
             int(matrix[0][c]) + int(matrix[len(matrix) - 1][c])
    return result


player1, player2 = input().split(", ")
size_of_dartboard = 7
dartboard = init_dartboard(size_of_dartboard)
player1_points = 501
player2_points = 501

players = {
    player1: player1_points,
    player2: player2_points
}

turns = 0

curr_player, other_player = player1, player2


while True:

    trow = input()[1:-1]

    if curr_player == player1:
        turns += 1

    row, column = map(int, trow.split(", "))

    if not in_dartboard(row, column, size_of_dartboard):
        curr_player, other_player = other_player, curr_player
        continue

    hit = dartboard[row][column]

    if hit.isdigit():
        players[curr_player] -= int(hit)
    elif hit == "D":
        players[curr_player] -= find_sum(row, column, dartboard) * 2
    elif hit == "T":
        players[curr_player] -= find_sum(row, column, dartboard) * 3
    elif hit == "B":
        break

    if players[curr_player] <= 0:
        break

    curr_player, other_player = other_player, curr_player

print(f"{curr_player} won the game with {turns} throws!")

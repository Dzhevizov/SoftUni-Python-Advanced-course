clothes = list(map(int, input().split()))
rack_capacity = int(input())

rack_count = 1
curr_capacity = rack_capacity

while clothes:
    curr_piece_of_clothing = clothes[-1]
    if curr_piece_of_clothing <= curr_capacity:
        curr_capacity -= curr_piece_of_clothing
        clothes.pop()
    else:
        rack_count += 1
        curr_capacity = rack_capacity

print(rack_count)

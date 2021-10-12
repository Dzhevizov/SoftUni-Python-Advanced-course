def combinate_chairs(people, chairs, curr_comb):
    if len(curr_comb) == chairs:
        print(", ".join(curr_comb))
        return

    for i in range(len(people)):
        curr_comb.append(people[i])
        combinate_chairs(people[i+1:], chairs, curr_comb)
        curr_comb.pop()


names = [name for name in input().split(", ")]
chairs_count = int(input())

combinate_chairs(names, chairs_count, [])

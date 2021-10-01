num_of_names = int(input())

usernames = set()

for _ in range(num_of_names):
    name = input()
    usernames.add(name)

for name in usernames:
    print(name)

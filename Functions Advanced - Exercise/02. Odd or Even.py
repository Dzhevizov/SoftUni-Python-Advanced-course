def print_sum(cmd, nums):
    parity = 0 if cmd == "Even" else 1
    print(sum(filter(lambda x: x % 2 == parity, nums)) * len(nums))


command = input()
numbers = [int(x) for x in input().split()]
print_sum(command, numbers)

nums = input().split()
rev_nums = []

while nums:
    rev_nums.append(nums.pop())

print(" ".join(rev_nums))

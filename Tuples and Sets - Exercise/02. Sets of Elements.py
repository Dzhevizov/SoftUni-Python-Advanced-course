first_length, second_length = map(int, input().split())

first = set()
second = set()

for _ in range(first_length):
    integer = int(input())
    first.add(integer)

for _ in range(second_length):
    integer = int(input())
    second.add(integer)

result = first.intersection(second)

for el in result:
    print(el)

numbers = [float(x) for x in input().split()]

dictionary = {}

for el in numbers:
    if el not in dictionary:
        dictionary[el] = 0
    dictionary[el] += 1

for number, count in dictionary.items():
    print(f"{number:.1f} - {count} times")

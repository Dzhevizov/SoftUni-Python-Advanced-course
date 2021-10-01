text = input()

dictionary = {}

for el in text:
    if el not in dictionary:
        dictionary[el] = 0
    dictionary[el] += 1

for letter, count in sorted(dictionary.items()):
    print(f"{letter}: {count} time/s")

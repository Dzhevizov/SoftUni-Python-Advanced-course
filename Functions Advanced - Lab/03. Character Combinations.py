def permutate_iterable(iterable, index):
    if index == len(iterable):
        print("".join(iterable))
        return

    for i in range(index, len(iterable)):
        iterable[i], iterable[index] = iterable[index], iterable[i]
        permutate_iterable(iterable, index + 1)
        iterable[i], iterable[index] = iterable[index], iterable[i]


text = list(input())
permutate_iterable(text, 0)

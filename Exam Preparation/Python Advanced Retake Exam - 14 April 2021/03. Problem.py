def flights(*args):
    result = {}
    for i in range(len(args)):
        if args[i] == "Finish":
            break
        if isinstance(args[i], int):
            continue
        if isinstance(args[i], str):
            if args[i] not in result:
                result[args[i]] = 0
            result[args[i]] += args[i + 1]
    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

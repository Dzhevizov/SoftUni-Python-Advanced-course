def generate_expressions(iterable, expression="", result=0):
    if not iterable:
        print(f"{expression}={result}")
        return

    generate_expressions(iterable[1:], expression + f"+{iterable[0]}", result+iterable[0])
    generate_expressions(iterable[1:], expression + f"-{iterable[0]}", result-iterable[0])


list_of_numbers = [int(x) for x in input().split(", ")]
generate_expressions(list_of_numbers)

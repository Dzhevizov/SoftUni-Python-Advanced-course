def operate(operator, *args):
    if operator == "+":
        result = 0
        for arg in args:
            result += arg
    elif operator == "-":
        result = args[0]
        for arg in args[1:]:
            result -= arg
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
    elif operator == "/":
        result = args[0]
        for arg in args[1:]:
            if not arg == 0:
                result /= arg

    return result


# print(operate("-", 8, 1, 2, 3))
print(operate("/", 24, 3, 4))

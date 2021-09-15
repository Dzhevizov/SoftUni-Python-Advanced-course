expression = list(input())

parentheses_indexes = []

for i, ch in enumerate(expression):
    if ch == "(":
        parentheses_indexes.append(i)
    elif ch == ")":
        opening_parentheses = parentheses_indexes.pop()
        closing_parentheses = i
        print("".join(expression[opening_parentheses:closing_parentheses + 1]))

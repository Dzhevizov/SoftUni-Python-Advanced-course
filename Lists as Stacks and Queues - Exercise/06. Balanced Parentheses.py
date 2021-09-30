sequence = list(input())

brackets = {
    '{': '}',
    '[': ']',
    '(': ')'
}

opening_brackets = []
is_balanced = True

for el in sequence:
    if el in brackets:
        opening_brackets.append(el)
    else:
        if not opening_brackets or el != brackets[opening_brackets[-1]]:
            print('NO')
            is_balanced = False
            break
        opening_brackets.pop()

if is_balanced:
    print('YES')
    
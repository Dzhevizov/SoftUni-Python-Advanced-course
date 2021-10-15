from basic_calculations import *


def math_operations(num1, sgn, num2):
    result = None
    if sgn == "+":
        result = add(num1, num2)
    elif sgn == "-":
        result = subtract(num1, num2)
    elif sgn == "*":
        result = multiply(num1, num2)
    elif sgn == "/" and not num2 == 0:
        result = divide(num1, num2)
    elif sgn == "^":
        result = power(num1, num2)
    return result


input_data = input().split()
number1 = float(input_data[0])
sign = input_data[1]
number2 = int(input_data[2])
print(f"{math_operations(number1, sign, number2):.2f}")

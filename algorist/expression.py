from typing import List, Union
from collections import deque
from operator import add, truediv, mul, sub

Precendence = {"+": 0, "-": 0, "/": 1, "*": 1, "^": 2}


def eval_postfix(expr=List[Union[float, str]]):
    stack = deque()
    for val in expr:
        if isinstance(val, (int, float)):
            stack.append(val)
        else:
            if val == "+":
                op = add
            elif val == "-":
                op = sub
            elif val == "*":
                op = mul
            elif val == "/":
                op = truediv
            else:
                raise ValueError(f"Operator={val} must be one of [+,-,*,/]")
            b = stack.pop()
            a = stack.pop()
            stack.append(op(a, b))
    return stack.pop()


def infix_to_postfix(expr=List[Union[float, str]]):
    output = []
    stack = deque()
    for val in expr:
        if isinstance(val, (float, int)):
            output.append(val)
            continue
        if val == "(":
            stack.append(val)
            continue
        if len(stack) == 0:
            stack.append(val)
            continue
        top = stack[-1]
        if val == ")":
            while top != "(":
                output.append(stack.pop())
                top = stack[-1]
            stack.pop()
            continue

        if top == "(" or Precendence[val] > Precendence[top]:
            stack.append(val)
            continue
        while top != "(" and Precendence[val] <= Precendence[top]:
            output.append(stack.pop())
            if len(stack) == 0:
                break
            top = stack[-1]
        stack.append(val)

    while len(stack) != 0:
        output.append(stack.pop())

    return output

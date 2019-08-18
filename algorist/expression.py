from typing import List, Union
from collections import deque
from operator import add, truediv, mul, sub


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

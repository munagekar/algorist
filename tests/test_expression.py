from algorist.expression import eval_postfix, infix_to_postfix


def test_eval_postfix():
    expr = [1, 2, "+"]
    assert eval_postfix(expr) == 3
    expr = [2, 3, 1, "*", "+", 9, "-"]
    assert eval_postfix(expr) == -4


def test_infix_to_postfix():
    a = infix_to_postfix([1, "+", 2, "*", "(", 3, "^", 4, "-", 5, ")", "^", "(", 6, "+", 7, "*", 8, ")", "-", 9])
    assert a == [1, 2, 3, 4, "^", 5, "-", 6, 7, 8, "*", "+", "^", "*", "+", 9, "-"]

from algorist.expression import eval_postfix


def test_eval_postfix():
    expr = [1, 2, "+"]
    assert eval_postfix(expr) == 3
    expr = [2, 3, 1, "*", "+", 9, "-"]
    assert eval_postfix(expr) == -4

from typing import Any, Callable


def identity(x: Any) -> Any:
    return x


def negate_func(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    return lambda x: -func(x)

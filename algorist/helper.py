from typing import Tuple, Any, Callable


def identity(x: Any) -> Any:
    return x


def negate_func(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    return lambda x: -func(x)


def stablize_func(func: Callable[[Any], Any]) -> Callable[[Tuple[Any, int]], Tuple[Any, int]]:
    return lambda x: (func(x[0]), x[1])


def stable_max(
    x: Tuple[Any, int], y: Tuple[Any, int], *args: Tuple[Any, int], key: Callable[[Any], Any] = identity
) -> Tuple[Any, int]:
    return max(x, y, *args, key=stablize_func(key))

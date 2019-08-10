from typing import Tuple, Any, Callable


def identity(x: Any) -> Any:
    return x


def stable_max(
    x: Tuple[Any, int], y: Tuple[Any, int], *args: Tuple[Any, int], key: Callable[[Any], Any] = identity
) -> Tuple[Any, int]:
    return max(x, y, *args, key=lambda z: (key(z[0]), z[1]))

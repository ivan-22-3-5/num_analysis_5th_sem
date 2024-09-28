from functools import partial
from typing import Callable


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def function(x: float) -> float:
    return x ** 3 - 4.1 * x ** 2 + 2.2 * x + 1.4


def validate_interval(interval: tuple[float, float], func: Callable[[float], float]) -> bool:
    start, end = interval
    if start > end:
        return False
    if func(start) * func(end) > 0:
        return False
    return True


def bisection(interval: tuple[float, float],
              func: Callable[[float], float],
              mid_func: Callable[[float, float, int], float],
              precision: float = 1e-4) -> float:
    if not validate_interval(interval, func):
        raise ValueError("Invalid interval")
    start, end = interval
    i = 0
    while True:
        mid = mid_func(start, end, i)
        if abs(start - mid) <= 2 * precision:
            break

        if func(start) * func(mid) > 0:
            start = mid
        else:
            end = mid
        i += 1
    return mid


def find_intervals(func: Callable[[float], float],
                   step: float,
                   domain: tuple[float, float]) -> list[tuple[float, float]]:
    intervals = []
    start, end = domain
    while start <= end:
        if func(start) * func(start + step) < 0:
            intervals.append((start, start + step))
        start += step
    return intervals


def find_roots(func: Callable[[float], float], mid_func: Callable[[float, float, int], float]) -> list[float]:
    intervals = find_intervals(func, 0.1, (-100, 100))
    roots = []
    for interval in intervals:
        root = bisection(interval, func, mid_func)
        roots.append(root)
    return roots


dichotomy_method = partial(find_roots, func=function, mid_func=lambda x, y, _: (x + y) / 2)
golden_ratio_method = partial(find_roots, func=function, mid_func=lambda x, y, _: x + (y-x) * 0.618)
fibonacci_method = partial(find_roots, func=function, mid_func=lambda x, y, i: x + (y-x) * (fibonacci(i + 2) / fibonacci(i + 4)))

from typing import Callable

import numpy as np

from src.point import Point
from src.approximation import build_polynomial


def f(x: float, y: float) -> float:
    return 0.2 * x ** 2 + 0.3 * (x ** 3 + 0.5 + y)


def test_func(x: float, y: float):
    return y * (x - 1) - (2 - 0.5 * x) * x


def euler(func: Callable, x0: float, y0: float, h: float, rng: tuple[float, float]):
    points: list[Point] = []
    x, y = x0, y0
    for _ in np.arange(x0, rng[1] + h, h):
        points.append(Point(x, y))
        x, y = x + h, y + h * func(x, y)

    return build_polynomial(points, 3)


def main():
    print(euler(test_func, 0, 1, 0.05, (0, 2)))


if __name__ == '__main__':
    main()

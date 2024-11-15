from typing import Callable
from src.point import Point
from src.approximation import build_polynomial


def f(x: float, y: float) -> float:
    return 0.2 * x ** 2 + 0.3 * (x ** 3 + 0.5 + y)


def test_func(x: float, y: float):
    return y * (x - 1) - (2 - 0.5 * x) * x


def euler(func: Callable, y0: float, h: float, rng: tuple[float, float]):
    points: list[Point] = []
    number_of_points = int((rng[1] - rng[0]) / h)
    x, y = rng[0], y0
    for _ in range(number_of_points + 1):
        points.append(Point(x, y))
        x, y = x + h, y + h * func(x, y)

    return build_polynomial(points, 3)


def main():
    print(euler(test_func, 1, 0.05, (0, 2)))


if __name__ == '__main__':
    main()

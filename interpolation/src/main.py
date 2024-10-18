import math
from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def build_lagrange_polynomial(points: list[Point]) -> sp.Add:
    x = sp.Symbol('x')
    result = 0
    for i in range(len(points)):
        result += points[i].y * math.prod(
            (x - points[j].x) / (points[i].x - points[j].x)
            for j in range(len(points)) if j != i)
    return result.expand()


def main():
    lagrange_polynomial = build_lagrange_polynomial([Point(-4, -2), Point(-3, 0), Point(-2, 1), Point(-1, -1), Point(0, -3)])
    print(lagrange_polynomial.subs('x', 1))


if __name__ == '__main__':
    main()

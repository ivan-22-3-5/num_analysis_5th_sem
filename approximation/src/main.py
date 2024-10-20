import json
from dataclasses import dataclass

import numpy as np
import sympy as sp


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def read_points(filename: str = 'data/points.json') -> list[Point]:
    with open(filename) as f:
        return [Point(*coordinates) for coordinates in json.load(f)]


def build_polynomial(points: list[Point], degree: int = 1):
    if not 1 <= degree <= 10:
        raise ValueError('Polynomial degree must be >= 1 and <= 10')

    lhs = np.array([
        [
            sum(map(lambda point: point.x ** p, points)) for p in range(degree + d, -1 + d, -1)
        ] for d in range(0, degree + 1)
    ])
    rhs = np.array([sum(map(lambda point: point.x ** p * point.y, points)) for p in range(degree + 1)])

    coefficients = np.linalg.solve(lhs, rhs)
    x = sp.Symbol('x')
    return sum(coefficients[-(p + 1)] * x ** p for p in range(degree, -1, -1))


def find_best_fit(points: list[Point], max_degree: int = 5):
    if not 1 <= max_degree <= 10:
        raise ValueError('Polynomial degree must be >= 1 and <= 10')

    best_error: float = float('inf')
    best_polynomial = None

    for degree in range(1, max_degree + 1):
        polynomial = build_polynomial(points, degree=degree)
        err = sum((point.y - polynomial.subs('x', point.x)) ** 2 for point in points)
        if err < best_error:
            best_error = err
            best_polynomial = polynomial

    return best_polynomial, best_error


def main():
    print(find_best_fit([
        Point(-4, -2),
        Point(-3, 0),
        Point(-2, 1),
        Point(-1, -1),
        Point(0, -3),
    ], max_degree=3))


if __name__ == '__main__':
    main()

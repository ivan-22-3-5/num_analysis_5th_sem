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


def calculate_distance(point1: Point, point2: Point) -> float:
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


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
    return sum(coefficients[-(p + 1)] * sp.Symbol('x') ** p for p in range(degree, -1, -1))


def main():
    print(build_polynomial([
        Point(-4, -2),
        Point(-3, 0),
        Point(-2, 1),
        Point(-1, -1),
        Point(0, -3),
    ], degree=3))


if __name__ == '__main__':
    main()

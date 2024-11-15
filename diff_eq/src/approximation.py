import numpy as np
import sympy as sp

from point import Point


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
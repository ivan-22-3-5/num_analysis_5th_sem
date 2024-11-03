import json
from dataclasses import dataclass

import matplotlib.pyplot as plt
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


def plot_polynomial(points: list[Point], degree: int = 1):
    polynomial = build_polynomial(points, degree)

    x_vals = np.linspace(min(point.x for point in points) - 1,
                         max(point.x for point in points) + 1,
                         100)

    y_vals = [polynomial.evalf(subs={sp.Symbol('x'): x}) for x in x_vals]

    x_points = [point.x for point in points]
    y_points = [point.y for point in points]

    fig = plt.figure(figsize=(10, 6))
    fig.patch.set_facecolor('#DAD5D1')

    plt.plot(x_vals, y_vals, label=f'Polynomial Degree {degree}', color='blue')
    plt.scatter(x_points, y_points, color='red', zorder=5, label='Data Points')
    plt.title(f'Polynomial Fit of Degree {degree}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


def main():
    pol, err = find_best_fit(read_points(), max_degree=4)
    print(f"Polynomial: {pol.evalf(3)}\n"
          f"Error: {err}")


if __name__ == '__main__':
    main()

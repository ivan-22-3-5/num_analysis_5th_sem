import json
import math
from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def read_points(filename: str = 'data/points.json') -> list[Point]:
    with open(filename) as f:
        return [Point(*coordinates) for coordinates in json.load(f)]


def build_lagrange_polynomial(points: list[Point]) -> sp.Add:
    x = sp.Symbol('x')
    n = len(points)
    result = 0
    for i in range(n):
        result += points[i].y * math.prod(
            (x - points[j].x) / (points[i].x - points[j].x)
            for j in range(n) if j != i)
    return result.expand()


def main():
    points = read_points()
    lagrange_polynomial = build_lagrange_polynomial(points)
    print(f"x = 5, y = {lagrange_polynomial.subs('x', 5)}",
          f"x = 5.5, y = {lagrange_polynomial.subs('x', 5.5)}",
          f"x = 6, y = {lagrange_polynomial.subs('x', 6)}",
          f"x = 7, y = {lagrange_polynomial.subs('x', 7)}",
          f"x = 7.5, y = {lagrange_polynomial.subs('x', 7.5)}",
          f"x = 8, y = {lagrange_polynomial.subs('x', 8)}",
          f"x = 9, y = {lagrange_polynomial.subs('x', 9)}",
          f"x = 9.5, y = {lagrange_polynomial.subs('x', 9.5)}",
          f"x = 10, y = {lagrange_polynomial.subs('x', 10)}",
          sep='\n')


if __name__ == '__main__':
    main()

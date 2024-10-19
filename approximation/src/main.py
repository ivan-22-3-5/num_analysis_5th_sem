import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def read_points(filename: str = 'data/points.json') -> list[Point]:
    with open(filename) as f:
        return [Point(*coordinates) for coordinates in json.load(f)]


def calculate_distance(point1: Point, point2: Point) -> float:
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


def calculate_sums(points: list[Point]):
    sums = {
        'sum_x_power_two': sum(map(lambda point: point.x ** 2, points)),
        'sum_x_power_three': sum(map(lambda point: point.x ** 3, points)),
        'sum_x_power_four': sum(map(lambda point: point.x ** 4, points)),
        'sum_x_power_five': sum(map(lambda point: point.x ** 5, points)),
        'sum_x_power_six': sum(map(lambda point: point.x ** 6, points)),
        'sum_xy': sum(map(lambda point: point.x * point.y, points)),
        'sum_x_power_two_y': sum(map(lambda point: point.x ** 2 * point.y, points)),
        'sum_x_power_three_y': sum(map(lambda point: point.x ** 3 * point.y, points)),
    }
    return sums


def main():
    points = read_points()
    print(calculate_sums(points))


if __name__ == '__main__':
    main()

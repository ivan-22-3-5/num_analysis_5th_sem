import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def read_points(filename: str = 'data/points.json') -> list[Point]:
    with open(filename) as f:
        return [Point(*coordinates) for coordinates in json.load(f)]


def main():
    points = read_points()


if __name__ == '__main__':
    main()

from typing import Callable


def simpson_integration():
    ...


def trapezoidal_integration():
    ...


def rectangular_integration(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += func((a + i * h) + h / 2)
    return integral * h


def main():
    print(f"{rectangular_integration(lambda x: 4 - x ** 2, 0, 2, 1000)=}")


if __name__ == '__main__':
    main()

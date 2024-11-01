from typing import Callable


def simpson_integration(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a) / n
    integral = func(a) + func(b)
    for i in range(1, int(n / 2)):
        integral += 4 * func(a + (2 * i - 1) * h)
    for i in range(1, int((n - 2) / 2)):
        integral += 2 * func(a + (i * 2) * h)
    return integral * h / 3


def trapezoidal_integration(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a) / n
    integral = func(a) + func(b) / 2
    for i in range(1, n):
        integral += func(a + i * h)
    return integral * h


def rectangular_integration(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += func((a + i * h) + h / 2)
    return integral * h


def main():
    print(f"{rectangular_integration(lambda x: 4 - x ** 2, 0, 2, 1000)=}")
    print(f"{trapezoidal_integration(lambda x: 4 - x ** 2, 0, 2, 1000)=}")
    print(f"{simpson_integration(lambda x: 4 - x ** 2, 0, 2, 1000)=}")


if __name__ == '__main__':
    main()

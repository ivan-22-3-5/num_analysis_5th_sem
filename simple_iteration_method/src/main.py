import json
from pathlib import Path

import numpy as np


def read_equations(filename: Path) -> tuple[np.ndarray, np.ndarray]:
    with open(filename) as f:
        data: dict[str, list] = json.load(f)
        return np.array(data["LHS"], np.float32), np.array(data["RHS"], np.float32)


def validate_data(matrix: np.ndarray, rhs: np.ndarray):
    rows, cols = matrix.shape
    if matrix.ndim != 2:
        raise np.linalg.LinAlgError("The array is not two dimensional!")
    if rows != cols:
        raise np.linalg.LinAlgError("The matrix is not square!")
    if np.linalg.det(matrix) == 0:
        raise np.linalg.LinAlgError("The matrix is singular!")
    if rhs.ndim != 1:
        raise np.linalg.LinAlgError("The right hand side is not a column vector!")
    if len(rhs) != rows:
        raise np.linalg.LinAlgError("The right hand side is not the same size as the left!")
    for i in range(rows):
        if abs(matrix[i, i]) <= np.abs(matrix[i]).sum() - abs(matrix[i, i]):
            raise np.linalg.LinAlgError(f"One of the diagonal elements is greater than sum of the other elements in the row!")


def solve_system(matrix: np.ndarray, rhs: np.ndarray,
                 start_vector: np.ndarray, precision_range: tuple[float, float] = (1e-6, 2e-6)) -> np.ndarray:
    validate_data(matrix, rhs)
    order, _ = matrix.shape

    previous_x_vector = start_vector
    while True:
        x_vector = np.array([rhs[i] - sum(matrix[i] * previous_x_vector) + matrix[i, i] * previous_x_vector[i]
                             for i in range(order)]) / matrix.diagonal()
        if precision_range[0] < np.max(np.abs(x_vector-previous_x_vector)) < precision_range[1]:
            break
        previous_x_vector = x_vector
    return x_vector


def main():
    matrix_path = Path("data", "system.json")
    if not matrix_path.exists():
        print("File with the matrix does not exist!")
        return
    matrix, rhs = read_equations(matrix_path)

    print(solve_system(matrix, rhs, start_vector=np.array([21, 1, 2, 0.5]), precision_range=(17e-6, 50e-6)))
    print(np.linalg.solve(matrix, rhs))


if __name__ == "__main__":
    main()

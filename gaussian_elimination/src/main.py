import json
from itertools import product
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


def solve_system(matrix: np.ndarray, rhs: np.ndarray) -> np.ndarray:
    validate_data(matrix, rhs)
    matrix = np.concatenate((matrix, rhs.reshape(-1, 1)), axis=1)
    rows, _ = matrix.shape
    for col, row in product(range(rows), range(rows)):
        if col != row and matrix[col, col] == 0:
            matrix[col] += matrix[row]

    for col, row in product(range(rows), range(rows)):
        if col != row:
            k = matrix[row, col] / matrix[col, col]
            matrix[row] = matrix[row] - k * matrix[col]
    matrix[:, -1] /= matrix.diagonal()

    return matrix[:, -1]


def main():
    matrix_path = Path("data", "system.json")
    if not matrix_path.exists():
        print("File with the matrix does not exist!")
        return
    matrix, rhs = read_equations(matrix_path)

    print(solve_system(matrix, rhs))
    print(np.linalg.solve(matrix, rhs))


if __name__ == "__main__":
    main()

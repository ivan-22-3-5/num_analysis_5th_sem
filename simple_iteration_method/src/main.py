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


def solve_system(matrix: np.ndarray, rhs: np.ndarray, start_vector: np.ndarray, precision: float = 1e-6):
    validate_data(matrix, rhs)


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

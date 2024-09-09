import json
from pathlib import Path

import numpy as np


def read_equations(filename: Path) -> tuple[np.matrix, np.ndarray]:
    with open(filename) as f:
        data = json.load(f)
        return np.matrix(data["LHS"], np.float32), np.array(data["RHS"], np.float32)


def validate_data(matrix: np.matrix, rhs: np.ndarray) -> tuple[bool, str]:
    rows, cols = matrix.shape
    if rows != cols:
        return False, "The matrix is not square!"
    if np.linalg.det(matrix) == 0:
        return False, "The matrix is singular!"
    if rhs.ndim != 1:
        return False, "The right hand side is not a column vector!"
    if len(rhs) != rows:
        return False, "The right hand side is not the same size as the left!"
    return True, ""


def main():
    matrix_path = Path("data", "system.json")
    if not matrix_path.exists():
        print("File with the matrix does not exist!")
        return
    matrix, rhs = read_equations(matrix_path)
    is_valid, validation_message = validate_data(matrix, rhs)
    if not is_valid:
        print(validation_message)


if __name__ == "__main__":
    main()

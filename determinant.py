from helpers import get_matrix


def main():
    matrix = get_matrix()

    answer = determinant(matrix)
    print(f"Determinant: {answer}")


def determinant(a: list[list[float]]) -> float:
    # Base case for 2x2 matrix
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    det = 0
    for c in range(len(a)):
        # Calculate the minor matrix
        minor = [row[:c] + row[c + 1 :] for row in a[1:]]
        # Recursive call to calculate determinant of the minor
        det += ((-1) ** c) * a[0][c] * determinant(minor)

    return det


if __name__ == "__main__":
    main()

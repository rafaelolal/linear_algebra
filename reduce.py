from helpers import get_matrix, print_matrix


def main():
    # input
    matrix: list[list[float]] = get_matrix()

    # default matrix for testing
    if not matrix:
        # matrix = [[0, 0, 3, 12], [0, 0, -1, -4], [0, 0, 0, 0], [2, 4, 2, 14]]
        matrix = [
            [1, 3, 3, 8, 5],
            [0, 1, 3, 10, 8],
            [0, 0, 0, -1, -4],
            [0, 0, 0, 2, 8],
        ]

    solve(matrix)
    print("Reduced echelon form:")
    print_matrix(matrix)


def solve(matrix: list[list[float]]) -> None:
    cur_row = 0
    pivot_cols: list[float] = []
    while cur_row < min(len(matrix), len(matrix[0])):
        # begin with the leftmost nonzero column
        # select a nonzero entry in the pivot column as a pivot
        pivot_row, leftmost_col = get_next_pivot_position(
            matrix, cur_row, cur_row
        )

        # repeat the process until there are no more nonzero columns
        if pivot_row is None and leftmost_col == float("inf"):
            break

        pivot_cols.append(leftmost_col)

        # interchange rows to move this entry into the pivot position
        swap_rows(matrix, pivot_row, cur_row)

        # use sum_rows to create zeros in all positions below the pivot
        pivot_value = matrix[cur_row][leftmost_col]
        for row in range(cur_row + 1, len(matrix)):
            # i know matrix[row][leftmost_column] != 0
            factor = -matrix[row][leftmost_col] / pivot_value
            sum_rows(matrix, row, cur_row, factor)

        cur_row += 1
        print(f"Step {cur_row}:")
        print_matrix(matrix)

    print("Echelon form:")
    print_matrix(matrix)

    # beginning with the rightmost pivot and working upward and to the left,
    # create zeros above each pivot
    lowest_pivot_row = len(matrix) - (len(matrix) - len(pivot_cols))
    for pivot_row in range(lowest_pivot_row - 1, -1, -1):
        pivot_col = pivot_cols[pivot_row]
        pivot_value = matrix[pivot_row][pivot_col]

        for j in range(pivot_row - 1, -1, -1):
            if pivot_value == 0:
                continue

            factor = -matrix[j][pivot_col] / pivot_value
            sum_rows(matrix, j, pivot_row, factor)

        # if a pivot is not 1, make it 1 via scale_row
        scale_row(matrix, pivot_row, 1 / pivot_value)


def swap_rows(
    matrix: list[list[float]], target_row: int, source_row: int
) -> None:
    matrix[target_row], matrix[source_row] = (
        matrix[source_row],
        matrix[target_row],
    )


def sum_rows(
    matrix: list[list[float]], target_row: int, addend_row: int, factor: float
) -> None:
    matrix[target_row] = [
        x + y * factor for x, y in zip(matrix[target_row], matrix[addend_row])
    ]


def scale_row(matrix: list[list[float]], target_row: int, factor: float):
    matrix[target_row] = [n * factor for n in matrix[target_row]]


def get_next_pivot_position(
    matrix: list[list[float]], start_row: int, start_col: int
) -> tuple[int | None, float]:
    pivot_col = float("inf")
    pivot_row = None

    for row in range(start_row, len(matrix)):
        attempt = float("inf")
        for col in range(start_col, len(matrix[0])):
            if matrix[row][col] != 0:
                attempt = col
                break

        if attempt < pivot_col:
            pivot_col = attempt
            pivot_row = row

    return pivot_row, pivot_col


if __name__ == "__main__":
    main()

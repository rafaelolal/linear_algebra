import re


def get_matrix() -> list[list[float]]:
    print("Enter space separated rows, blank to end.")
    matrix: list[list[float]] = []
    required_length = None
    while True:
        row = input()
        row = row.strip()
        # Remove all repeated spaces
        row = re.sub(" +", " ", row)

        if not row:
            break

        row = list(map(float, row.split(" ")))

        if required_length is None:
            required_length = len(row)

        if len(row) != required_length:
            print(
                f'Rows must have the same number of elements: "{required_length}".'
            )
            continue

        matrix.append(row)

    return matrix


def print_matrix(matrix: list[list[float]]) -> None:
    matrix = [[my_round(x, 3) for x in row] for row in matrix]
    longest_number = max([len(str(x)) for row in matrix for x in row])
    output = ""
    for row in matrix:
        for x in row:
            output += f"{x:>{longest_number}} "

        output.strip()
        output += "\n"

    print(output)


def my_round(x: float, digits: int):
    # I created this function because round(3.000, 3) = 3.0
    if x == int(x):
        return int(x)

    return round(x, digits)

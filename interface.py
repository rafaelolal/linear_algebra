from helpers import get_matrix
from reduce import print_matrix, scale_row, sum_rows, swap_rows


def main():
    matrix = get_matrix()
    swap_command = "swap <target_row> <source_row>"
    sum_command = "sum <target_row> <addend_row> <factor>"
    scale_command = "scale <target_row> <factor>"
    print(f"Commands:\n{swap_command}\n{sum_command}\n{scale_command}")
    print("Enter command and arguments, blank to end.")
    while True:
        command = input()
        if command == "":
            break

        if "swap" in command:
            _, target_row, source_row = command.split()
            target_row = int(target_row)
            source_row = int(source_row)

            # Perform the swap
            swap_rows(matrix, target_row, source_row)
            print("Matrix after swap:")
            print_matrix(matrix)

        elif "sum" in command:
            _, target_row, addend_row, factor = command.split()
            target_row = int(target_row)
            addend_row = int(addend_row)
            factor = float(factor)
            # Perform the sum operation
            sum_rows(matrix, target_row, addend_row, factor)
            print("Matrix after sum:")
            print_matrix(matrix)

        elif "scale" in command:
            _, target_row, factor = command.split()
            target_row = int(target_row)
            factor = float(factor)

            # Perform the scale operation
            scale_row(matrix, target_row, factor)
            print("Matrix after scaling:")
            print_matrix(matrix)

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

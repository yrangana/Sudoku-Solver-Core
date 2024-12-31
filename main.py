from src.solver import solve_sudoku_with_timeout


def display_grid(grid):
    """
    Display the Sudoku grid in a readable format.
    """
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        print("Invalid or unsolvable puzzle.")
        return

    for row in grid:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))


def get_default_puzzle():
    """
    Return a default Sudoku puzzle.
    """
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


def get_user_input_puzzle():
    """
    Get a Sudoku puzzle from user input.
    """
    print("Enter your Sudoku puzzle row by row, using 0 for empty cells.")
    user_puzzle = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != 9 or not all(0 <= num <= 9 for num in row):
                    raise ValueError
                user_puzzle.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter exactly 9 numbers between 0 and 9.")
    return user_puzzle


if __name__ == "__main__":
    # Ask the user if they want to use the default puzzle or input their own
    use_default = (
        input("Do you want to use the default Sudoku puzzle? (yes/y/no): ")
        .strip()
        .lower()
    )

    if use_default in ["yes", "y"]:
        puzzle = get_default_puzzle()
    else:
        puzzle = get_user_input_puzzle()

    # Ask the user to provide a timeout value
    while True:
        try:
            timeout = int(
                input("Enter the timeout in seconds for solving the puzzle: ").strip()
            )
            if timeout <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid timeout. Please enter a positive integer.")

    print("\nAttempting to solve the following Sudoku puzzle:")
    display_grid(puzzle)

    try:
        # Debugging: Print the raw return value of the solver
        solution = solve_sudoku_with_timeout(puzzle, timeout)
        print("\nSolver returned:")
        print(solution)

        if solution and isinstance(solution, list):
            print("\nSolved Sudoku puzzle:")
            display_grid(solution)
        else:
            print("\nNo solution found for the given Sudoku puzzle.")
    except TimeoutError:
        print(
            f"\nThe solver could not solve the puzzle within the timeout limit of {timeout} seconds."
        )

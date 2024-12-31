from src.solver import solve_sudoku


def display_grid(grid):
    """
    Display the Sudoku grid in a readable format.
    """
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
                if len(row) != 9 or any(cell < 0 or cell > 9 for cell in row):
                    raise ValueError
                user_puzzle.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter exactly 9 numbers between 0 and 9.")
    return user_puzzle


def solve_and_display(puzzle_grid):
    """
    Solve the given puzzle and display the result.
    """
    print("\nOriginal Puzzle:")
    display_grid(puzzle_grid)

    if solve_sudoku(puzzle_grid):
        print("\nSolved Puzzle:")
        display_grid(puzzle_grid)
    else:
        print("\nNo solution exists.")


if __name__ == "__main__":
    print("Sudoku Solver\n")

    # Prompt user for default or custom puzzle
    use_default_puzzle = input("Use default puzzle? (y/n): ").strip().lower() == "y"
    input_puzzle = (
        get_default_puzzle() if use_default_puzzle else get_user_input_puzzle()
    )

    # Solve and display the puzzle
    solve_and_display(input_puzzle)

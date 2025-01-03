import concurrent.futures


# Exception for handling timeouts
class TimeoutException(Exception):
    """Custom exception for handling timeouts."""


def is_valid_grid(board):
    """
    Validate if the input grid is a 9x9 list of integers.

    Args:
        board (list[list[int]]): Sudoku grid.

    Returns:
        bool: True if the grid is valid, False otherwise.
    """
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    if not all(
        isinstance(cell, int) and 0 <= cell <= 9 for row in board for cell in row
    ):
        return False
    return True


def is_valid(board, row, col, num):
    """
    Check if placing 'num' in board[row][col] is valid.

    Args:
        board (list[list[int]]): 9x9 Sudoku grid.
        row (int): Row index of the cell.
        col (int): Column index of the cell.
        num (int): Number to place in the cell.

    Returns:
        bool: True if the number can be placed, False otherwise.
    """
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def is_valid_puzzle(puzzle):
    """
    Validate the Sudoku puzzle to ensure it follows basic rules.

    Args:
        puzzle (list): 9x9 Sudoku grid.

    Returns:
        bool: True if valid, False otherwise.
    """
    for row in puzzle:
        if not is_valid_group(row):
            return False

    for col in zip(*puzzle):  # Transpose to check columns
        if not is_valid_group(col):
            return False

    # Check 3x3 sub-grids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                puzzle[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not is_valid_group(box):
                return False

    return True


def is_valid_group(group):
    """
    Check if a row, column, or box contains no duplicates (excluding zeros).

    Args:
        group (list): A group of 9 numbers.

    Returns:
        bool: True if valid, False otherwise.
    """
    numbers = [num for num in group if num != 0]
    return len(numbers) == len(set(numbers))


def solve_sudoku_helper(board):
    """Recursive helper function to solve the Sudoku puzzle."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku_helper(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def solve_sudoku_with_timeout(board, timeout=10):
    """Solve the Sudoku puzzle with a timeout."""
    if not is_valid_grid(board):
        raise ValueError("Invalid Sudoku grid. Must be a 9x9 grid with integers 0-9.")

    if not is_valid_puzzle(board):
        raise ValueError(
            "Invalid Sudoku puzzle. This puzzle does not have an solution."
        )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(solve_sudoku_helper, board)
        try:
            if future.result(timeout=timeout):
                return board
            else:
                raise TimeoutException(
                    "Unable to solve the puzzle within the given time"
                )
        except concurrent.futures.TimeoutError:
            raise TimeoutException(  # pylint: disable=W0707
                "Timeout exceeded while solving the puzzle"
            )

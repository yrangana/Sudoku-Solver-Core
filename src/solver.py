import signal


# Exception for handling timeouts
class TimeoutException(Exception):
    """Custom exception for handling timeouts."""


# Signal handler to raise timeout exception
def timeout_handler(signum, frame):
    raise TimeoutException("Timeout exceeded while solving the puzzle")


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


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.

    Args:
        board (list[list[int]]): 9x9 Sudoku grid with 0 for empty cells.

    Returns:
        bool: True if the puzzle is solvable, otherwise False.
    """
    if not is_valid_grid(board):
        raise ValueError("Invalid Sudoku grid. Must be a 9x9 grid with integers 0-9.")

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True


def solve_sudoku_with_timeout(puzzle, timeout=5):
    """
    Solve the Sudoku puzzle with a timeout.

    Args:
        puzzle (list): 9x9 Sudoku grid.
        timeout (int): Time limit in seconds.

    Returns:
        list[list[int]]: Solved Sudoku grid if solved within timeout.
        None: If unsolvable or if timeout exceeded.
    """
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)  # Start the timer
    try:
        # Create a copy of the puzzle to avoid modifying the original
        board = [row[:] for row in puzzle]
        if solve_sudoku(board):  # Call your existing solver logic
            signal.alarm(0)  # Cancel the alarm on success
            return board  # Return the solved board
        signal.alarm(0)  # Cancel the alarm on failure
        return None  # Return None if unsolvable
    except TimeoutException:
        signal.alarm(0)  # Ensure the alarm is cancelled after timeout
        return None  # Return None if timeout exceeded

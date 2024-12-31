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

    Example:
        >>> puzzle = [
        ...     [5, 3, 0, 0, 7, 0, 0, 0, 0],
        ...     [6, 0, 0, 1, 9, 5, 0, 0, 0],
        ...     ...
        ... ]
        >>> solve_sudoku(puzzle)
        True
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

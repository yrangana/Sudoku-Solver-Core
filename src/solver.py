def is_valid(board, row, col, num):
    """Check if placing 'num' in board[row][col] is valid."""
    for i in range(9):
        # Check row and column
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

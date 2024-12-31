[![Makefile CI](https://github.com/yrangana/Sudoku-Solver-Core/actions/workflows/makefile.yml/badge.svg)](https://github.com/yrangana/Sudoku-Solver-Core/actions/workflows/makefile.yml)

# Sudoku Solver Core

This is the **core module** of a Sudoku solver project. It provides the logic for solving 9x9 Sudoku puzzles using an efficient backtracking algorithm. This module is designed to be part of a larger project that includes features like OCR and image processing for extracting Sudoku puzzles from images.

---

## Features

- Solve 9x9 Sudoku puzzles using a backtracking algorithm.
- Validate puzzle input for correctness and consistency.
- Display puzzles in a user-friendly format.
- Designed for integration with other modules (e.g., OCR, image processing).

---

## Setup

### Prerequisites
- Python 3.10 or higher
- Virtual environment (recommended)

### Installation

#### Install Runtime Dependencies
To use the Sudoku Solver Core package:
```bash
pip install git+https://github.com/yrangana/Sudoku-Solver-Core.git@main
```

#### Install Development Dependencies
To contribute or run tests, install with development dependencies:
```bash
pip install git+https://github.com/yrangana/Sudoku-Solver-Core.git@main[dev]
```

### Local Development
For local development, clone the repository and install it in editable mode:
```bash
git clone https://github.com/yrangana/Sudoku-Solver-Core.git
cd Sudoku-Solver-Core
pip install -e .[dev]
```

---

## Usage

1. Import and use the Sudoku Solver Core in your Python project:
   ```python
   from src.solver import solve_sudoku

   puzzle = [
       [5, 3, 0, 0, 7, 0, 0, 0, 0],
       [6, 0, 0, 1, 9, 5, 0, 0, 0],
       ...
   ]

   if solve_sudoku(puzzle):
       print("Solved Puzzle:", puzzle)
   else:
       print("No solution exists.")
   ```

---

## Dependencies

### Runtime
- None (currently no runtime dependencies)

### Development
- `black`: Code formatting
- `click`: CLI support
- `ipython`: Interactive shell
- `pylint`: Code linting
- `pytest`: Testing framework
- `setuptools`: Packaging and build tool

---

## Contributing

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/yrangana/Sudoku-Solver-Core.git
   ```
2. Install dependencies for development:
   ```bash
   pip install -e .[dev]
   ```
3. Run tests to verify:
   ```bash
   pytest
   ```

### Package Installation
- Install the package in other projects using:
  ```bash
  pip install git+https://github.com/yrangana/Sudoku-Solver-Core.git@main
  ```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- Thanks to the open-source community for Python and Sudoku solving resources.

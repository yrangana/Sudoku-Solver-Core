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

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Virtual environment (recommended)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yrangana/sudoku-solver-core.git
   cd sudoku-solver-core
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\\Scripts\\activate`
   ```

3. Install dependencies:
   ```bash
   make install
   ```

---

## Usage

1. Run the `main.py` file:
   ```bash
   make run
   ```

2. Choose to use the default puzzle or input your own puzzle.

3. Follow the prompts for input:
   - Enter each row of the puzzle as space-separated numbers.
   - Use `0` for empty cells.

### Example

**Input Puzzle**:
```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

**Solved Puzzle**:
```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

---

## Makefile Commands

This project includes a `Makefile` for common tasks:

- **Install Dependencies**:
  ```bash
  make install
  ```

- **Run the Project**:
  ```bash
  make run
  ```

- **Test the Project**:
  ```bash
  make test
  ```

- **Format Code**:
  ```bash
  make format
  ```

- **Lint Code**:
  ```bash
  make lint
  ```

- **Clean Temporary Files**:
  ```bash
  make clean
  ```

---

## Tests

### Running Tests

To run the test suite, execute:
```bash
make test
```

### Test Cases

The test suite includes:
- Valid Sudoku puzzles.
- Invalid grids (e.g., non-9x9 grids, non-integer entries).
- Unsolvable puzzles.

---

## Contributing

This module is part of a larger project. Contributions are welcome to enhance the core logic or integrate it with other features.

### How to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- Thanks to the open-source community for Python and Sudoku solving resources.

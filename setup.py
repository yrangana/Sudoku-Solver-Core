from setuptools import setup, find_packages

setup(
    name="sudoku_solver_core",
    version="0.2.1",
    description="Core module for solving Sudoku puzzles",
    author="Yasiru Rangana",
    url="https://github.com/yrangana/Sudoku-Solver-Core",
    packages=find_packages(),  #  include all Python packages
    install_requires=[],  # runtime dependencies here if any
    extras_require={
        "dev": [
            "black==24.10.0",
            "click==8.1.8",
            "ipython==8.31.0",
            "pylint==3.3.3",
            "pytest==8.3.4",
            "setuptools==75.6.0",
        ]
    },  # Development dependencies
    python_requires=">=3.10",
)

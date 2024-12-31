install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black  *.py src/*.py tests/*.py

lint:
	pylint --disable=R,C *.py src/*.py tests/*.py

run:
	python main.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + &&\
	find . -type f -name "*.pyc" -delete &&\
	find . -type f -name "*.pyo" -delete

help:
	@echo "Available commands:"
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run tests"
	@echo "  make format      - Format code with black"
	@echo "  make lint        - Lint code with pylint"
	@echo "  make run         - Run the main script"
	@echo "  make clean       - Clean up temporary files"

all: help install lint format test clean
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black  *.py src/*.py tests/*.py

lint:
	pylint --disable=R,C *.py src/*.py tests/*.py

all: install lint format test
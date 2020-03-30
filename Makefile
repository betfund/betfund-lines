.PHONY: black
black:
	black lines

.PHONY: tests
tests:
	pytest -vv --cov=lines --cov-report term-missing

.PHONY: lint
lint:
	pylint -f colorized -d all -r y lines/ tests setup.py

.PHONY: flake
flake:
	flake8 lines

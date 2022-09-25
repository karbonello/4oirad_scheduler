.PHONY: pretty validate
DIRS = dom_quries

pretty:  ## code prettifying
	poetry run black .
	poetry run isort .


validate:  ## Code validation
	make flake8
	make mypy
	make pylint

flake8:
	poetry run flake8 --jobs 4 --max-line-length 88 --statistics --show-source $(DIRS)

mypy:
	poetry run mypy --show-error-codes $(DIRS)

pylint:
	poetry run pylint --jobs 4 --rcfile=setup.cfg $DIRS

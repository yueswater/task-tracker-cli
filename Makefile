POETRY ?= poetry

.PHONY: install test coverage clean

tree:
	tree > tree.txt

fmt:
	$(POETRY) run autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r .
	$(POETRY) run isort .
	$(POETRY) run black .

lint:
	$(POETRY) run flake8 .

test:
	$(POETRY) run pytest $(ARGS)

ptw:
	$(POETRY) run pytest-watch

install:
	$(POETRY) install

coverage:
	$(POETRY) run pytest --cov --cov-report=term-missing $(ARGS)

clean:
	rm -rf .pytest_cache .coverage htmlcov
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;

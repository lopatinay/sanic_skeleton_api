.PHONY: compile-versions
compile-versions:
	pip-compile -v --output-file requirements/requirements.txt requirements/requirements.in
	pip-compile -v --output-file requirements/dev_requirements.txt requirements/requirements.txt requirements/dev_requirements.in


.PHONY: flake
flake:
	flake8

.PHONY: test
test:
	py.test tests

.PHONY: coverage
coverage:
	coverage run -m py.test -v --ignore=venv tests/
	coverage report

.PHONY: check
check: flake coverage


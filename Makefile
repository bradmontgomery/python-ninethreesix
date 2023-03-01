.PHONY: all
all:
	build

.PHONY: build
build:
	python -m build

.PHONY: requirements
requirements:
	pip install --upgrade pip
	pip install --upgrade pip-tools
	pip install --upgrade setuptools
	pip install --upgrade build
	pip-compile -rU --no-emit-index-url requirements.in

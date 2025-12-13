.PHONY: all
all:
	build

.PHONY: build
build:
	uv build

.PHONY: install
install:
	uv sync

.PHONY: upload
upload:
	uv run twine upload dist/*

.PHONY: clean
clean:
	rm -rf dist/
	rm -rf python_ninethreesix.egg-info
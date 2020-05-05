SHELL = /bin/bash

.PHONY: help install build tests publish-test
.DEFAULT_GOAL = help

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install:  ## Install package deps locally
	poetry install --extras "dev"

build:  ## Build package
	poetry build

tests:  ## Run tests
	poetry run pytest


coverage:  ## Run tests with coverage
	poetry run coverage run -m pytest
	poetry run coverage report

safety:  ## Check installed dependencies for known security vulnerabilities
	poetry export --format=requirements.txt --without-hashes --output=requirements.txt
	poetry run safety check --full-report --file=requirements.txt
	rm requirements.txt

publish-test: test build ## Publish package to the test.pypi.org
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi

publish: test build  ## Publish package
	poetry publish

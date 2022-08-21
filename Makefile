PATH := .venv/bin:$(PATH)
PYPI ?= pypi
VAULT_TOKEN ?= $(shell cat ~/.vault-token 2> /dev/null)
export BUILD_TAG := $(shell git describe --tags --abbrev=0)

ifneq ($(VAULT_TOKEN),)
export TWINE_PASSWORD := $(shell curl -H 'x-vault-token: $(VAULT_TOKEN)' $(VAULT_ADDR)$(VAULT_PATH) | jq -r .data.data.password)
export TWINE_USERNAME := $(shell curl -H 'x-vault-token: $(VAULT_TOKEN)' $(VAULT_ADDR)$(VAULT_PATH) | jq -r .data.data.username)
endif

.PHONY: build
build: venv
	pip install swagger_to
	curl -L https://web.homechart.app/swagger.yaml -o swagger.yaml
	swagger_to_py_client.py --swagger_path swagger.yaml --outpath ./src/homechart.py --force

.PHONY: release
release: venv
	pip install setuptools twine wheel
	python setup.py sdist bdist_wheel
	twine upload -r $(PYPI) dist/*

.PHONY: venv
venv:
	python -m venv .venv

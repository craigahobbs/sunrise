# Licensed under the MIT License
# https://github.com/craigahobbs/sunrise/blob/main/LICENSE

.DEFAULT_GOAL := help


# Download pylintrc
define WGET
ifeq '$$(wildcard $(notdir $(1)))' ''
$$(info Downloading $(notdir $(1)))
_WGET := $$(shell $(call WGET_CMD, $(1)))
endif
endef
WGET_CMD = if which wget; then wget -q -c $(1); else curl -f -Os $(1); fi
$(eval $(call WGET, https://raw.githubusercontent.com/craigahobbs/python-build/main/pylintrc))


# Windows support
VENV_BIN := bin
VENV_PYTHON := python3
ifneq '$(NO_DOCKER)' ''
ifeq '$(OS)' 'Windows_NT'
ifeq ($(shell python3 -c "import sysconfig; print(sysconfig.get_preferred_scheme('user'))"),nt_user)
VENV_BIN := Scripts
VENV_PYTHON := python.exe
endif
endif
endif


# Python image
PYTHON_IMAGE ?= python:3
ifeq '$(NO_DOCKER)' ''
PYTHON_RUN := docker run -i --rm -u `id -g`:`id -g` -v `pwd`:`pwd` -w `pwd` $(PYTHON_IMAGE)
endif
PYTHON_ENV := $(PYTHON_RUN) build/venv/$(VENV_BIN)/$(VENV_PYTHON)


# By default generate two years, this year and next year
NYEARS ?= 1


.PHONY: help
help:
	@echo "usage: make [clean|commit|data|lint|superclean]"


.PHONY: clean
clean:
	rm -rf build/ pylintrc


.PHONY: superclean
superclean: clean
ifeq '$(NO_DOCKER)' ''
	-docker rmi -f $(PYTHON_IMAGE)
endif


.PHONY: commit
commit: lint data


.PHONY: gh-pages
gh-pages:


.PHONY: data
data: build/venv.build
	$(PYTHON_ENV) sunrise.py$(if $(YEAR), -y $(YEAR))$(if $(NYEARS), -n $(NYEARS)) > sunrise.csv


.PHONY: lint
lint: build/venv.build
	$(PYTHON_ENV) -m pylint --disable='missing-function-docstring, missing-module-docstring' sunrise.py


build/venv.build:
	mkdir -p build
	$(PYTHON_RUN) python3 -m venv --upgrade-deps build/venv
	$(PYTHON_ENV) -m pip install ephem pylint pytz
	touch $@

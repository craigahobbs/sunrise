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


.PHONY: help
help:
	@echo "usage: make [clean|data|help|lint]"


.PHONY: clean
clean:
	rm -rf build/


.PHONY: superclean
superclean: clean


.PHONY: commit
commit: lint data


.PHONY: data
data: build/venv.build
	build/venv/bin/python3 sunrise.py > sunrise.csv


.PHONY: lint
lint: build/venv.build
	build/venv/bin/python3 -m pylint --disable='missing-function-docstring, missing-module-docstring' sunrise.py


build/venv.build:
	mkdir -p build
	python3 -m venv build/venv
	build/venv/bin/pip install -U pip setuptools
	build/venv/bin/pip install ephem pylint pytz
	touch $@

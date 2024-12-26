# clip - IP address geolocation data fetcher
# See LICENSE file for copyright and license details.

# Use bash to support sourcing script files
SHELL:=/bin/bash

# Directory to install the compiled clip binary
BIN_DIR = /usr/local/bin

# We need a Python virtual environment to install the local
# dependencies, but the only way to make sure one exists in
# a Makefile is to use one of its sub-files, since directories
# aren't supported as dependency targets in Make.
VENV_DIR = lib/venv
VENV_SRC = ${VENV_DIR}/bin/activate
VENV = ${VENV_DIR}/pyvenv.cfg

# PyInstaller build options
PYINST_OPTS = -F -n clip --specpath src --distpath . --log-level ERROR

clip: ${VENV}
	source ${VENV_SRC}; pyinstaller ${PYINST_OPTS} src/main.py

${VENV}:
	python -m venv ${VENV_DIR}
	source ${VENV_SRC}; pip install -q -r lib/requirements.txt

install: clip
	mkdir -p ${BIN_DIR}
	cp clip ${BIN_DIR}/clip
	chmod 0755 ${BIN_DIR}/clip

uninstall:
	rm -f ${BIN_DIR}/clip

clean:
	rm -rf clip src/clip.spec build/

.PHONY: install uninstall clean

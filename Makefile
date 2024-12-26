# clip - IP address geolocation data fetcher
# See LICENSE file for copyright and license details.

# Use bash to support sourcing script files
SHELL:=/bin/bash

# Directory to install the compiled clip binary. Should be a
# directory included in your $PATH variable.
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

# Source the virtual environment and run pyinstaller with opts
# to compile the script
clip: ${VENV}
	source ${VENV_SRC}; pyinstaller ${PYINST_OPTS} src/main.py

# Create a virtual environment and then install the dependencies
# in requirements.txt
${VENV}:
	python -m venv ${VENV_DIR}
	source ${VENV_SRC}; pip install -q -r lib/requirements.txt

# After clip is compiled with PyInstaller, make sure the BIN_DIR
# exists, then put a copy of the clip binary into it, and change
# its permissions to match the location.
install: clip
	mkdir -p ${BIN_DIR}
	cp clip ${BIN_DIR}/clip
	chmod 0755 ${BIN_DIR}/clip

# Delete the copy of the clip binary from the BIN_DIR
uninstall:
	rm -f ${BIN_DIR}/clip

# Delete any built clip binary, the spec file, and build files.
clean:
	rm -rf clip src/clip.spec build/

.PHONY: install uninstall clean

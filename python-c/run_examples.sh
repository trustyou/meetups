#!/usr/bin/env bash

set -e

# do "pip install -r requirements.txt" before first run. It's nice to run this in a virtualenv

# install and run artihmetic module as smoke test

pushd . >/dev/null
cd arithmeticmodule
./setup.py install
python -c "import arithmetic; print(arithmetic.add(1, 1337))"
popd >/dev/null

# install quick module for later test

pushd . >/dev/null
cd quickmodule
./setup.py install
popd >/dev/null

# test all different implementations

./test_quicksort.py

# time them!

echo "*** Timing different implementations of Quicksort"

./time_quicksort.py time python
./time_quicksort.py time python2
./time_quicksort.py time c
./time_quicksort.py time cython
./time_quicksort.py time cython2

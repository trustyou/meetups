#!/usr/bin/env python

from distutils.core import setup, Extension

module = Extension("quick", sources=["quickmodule.c"])

setup(
	name="Quicksort",
	version="1.0",
	ext_modules=[module]
)

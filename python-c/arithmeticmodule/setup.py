#!/usr/bin/env python

from distutils.core import setup, Extension

module = Extension("arithmetic", sources=["arithmeticmodule.c"])

setup(
	name="Arithmetic",
	version="1.0",
	ext_modules=[module]
)

#!/usr/bin/env python

def get_args():
	from argparse import ArgumentParser
	argp = ArgumentParser("Test Quicksort!")
	argp.add_argument("action", choices=("profile", "time"))
	argp.add_argument("impl", choices=("python", "python2", "c", "cython", "cython2"))
	args = argp.parse_args()
	return args

if __name__ == "__main__":

	import random

	args = get_args()

	# prepare setup & test methods for timing algorithms

	xs = range(10000)
	def setup():
		global xs
		random.seed("l33t")
		random.shuffle(xs)

	if args.impl == "python":
		from quicksort import quicksort
		def sort():
			# need to make a copy since some algorithms modify in place
			_xs = xs[:]
			quicksort(_xs)
	elif args.impl == "python2":
		from quicksort import quicksort2
		def sort():
			_xs = xs[:]
			quicksort2(_xs)
	elif args.impl == "c":
		import quick
		def sort():
			_xs = xs[:]
			quick.quicksort(_xs)
	elif args.impl == "cython":
		import pyximport; pyximport.install()
		import quick_cython
		def sort():
			_xs = xs[:]
			quick_cython.quicksort(_xs)
	elif args.impl == "cython2":
		import pyximport; pyximport.install()
		import quick_cython_2
		def sort():
			_xs = xs[:]
			quick_cython_2.quicksort(_xs)

	# profile

	if args.action == "profile":
		import cProfile
		import pstats
		import sys
		
		pr = cProfile.Profile()
		pr.enable()
		setup()
		for _ in xrange(10):
			sort()
		pr.disable()

		stats = pstats.Stats(pr, stream=sys.stdout).sort_stats("time")
		stats.print_stats()

	# time

	elif args.action == "time":
		import timeit

		print "Time for", args.impl, timeit.timeit(stmt=sort, setup=setup, number=100)


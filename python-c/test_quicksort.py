#!/usr/bin/env python

import unittest

class QuicksortTestCase(unittest.TestCase):

	def test_quicksort(self):

		from quicksort import quicksort
		
		l = [5, 1, 3, 5, 2]
		self.assertEqual(sorted(l), quicksort(l))

	def test_quicksort2(self):

		from quicksort import quicksort2
		
		l = [3, 2, 5, 1, 2, 5]
		quicksort2(l)
		self.assertEqual(sorted(l), l)

	def test_c_quicksort(self):

		from quick import quicksort
		
		l = [3, 2, 5, 1, 2, 5]
		self.assertEqual(sorted(l), quicksort(l))

	def test_cython_quicksort(self):

		import pyximport; pyximport.install()
		import quick_cython
		
		l = [5, 1, 3, 5, 2]
		self.assertEqual(sorted(l), quick_cython.quicksort(l))

	def test_cython2_quicksort(self):

		import pyximport; pyximport.install()
		import quick_cython_2
		
		l = [3, 2, 5, 1, 2, 5]
		quick_cython_2.quicksort(l)
		self.assertEqual(sorted(l), l)

if __name__ == "__main__":

	unittest.main()

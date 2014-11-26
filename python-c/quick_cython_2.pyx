cdef partition(xs, int left, int right, int pivot_index):
	cdef int pivot = xs[pivot_index]
	cdef int el
	xs[pivot_index], xs[right] = xs[right], xs[pivot_index]
	pivot_index = left
	for i in xrange(left, right):
		el = xs[i]
		if el <= pivot:
			xs[i], xs[pivot_index] = xs[pivot_index], xs[i]
			pivot_index += 1
	xs[pivot_index], xs[right] = xs[right], xs[pivot_index]
	return pivot_index

def quicksort(xs, left=0, right=None):
	if right is None:
		right = len(xs) - 1
	if left < right:
		middle = (left + right) / 2

		pivot_index = partition(xs, left, right, middle)

		quicksort(xs, left, pivot_index - 1)
		quicksort(xs, pivot_index + 1, right)

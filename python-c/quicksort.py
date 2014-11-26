# first implementation: Pythonic quicksort

def quicksort(xs):

	if len(xs) <= 1:
		return xs

	middle = len(xs) / 2
	pivot = xs[middle]
	del xs[middle]

	left, right = [], []
	for x in xs:
		append_to = left if x < pivot else right
		append_to.append(x)
	return quicksort(left) + [pivot] + quicksort(right)

# second implementation: C-like quicksort in Python

def partition(xs, left, right, pivot_index):
	pivot = xs[pivot_index]
	xs[pivot_index], xs[right] = xs[right], xs[pivot_index]
	pivot_index = left
	for i in xrange(left, right):
		if xs[i] <= pivot:
			xs[i], xs[pivot_index] = xs[pivot_index], xs[i]
			pivot_index += 1
	xs[pivot_index], xs[right] = xs[right], xs[pivot_index]
	return pivot_index	

def quicksort2(xs, left=0, right=None):
	if right is None:
		right = len(xs) - 1
	if left < right:
		middle = (left + right) / 2

		pivot_index = partition(xs, left, right, middle)

		quicksort2(xs, left, pivot_index - 1)
		quicksort2(xs, pivot_index + 1, right)

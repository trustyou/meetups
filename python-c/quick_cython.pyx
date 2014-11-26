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

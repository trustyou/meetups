#include <Python.h>

#define SWAP(x,y) {int tmp = x; x = y; y = tmp;}

int partition(int* xs, int left, int right, int pivotIndex) {
	int i;
	int pivot = xs[pivotIndex];
	SWAP(xs[pivotIndex], xs[right]);
	pivotIndex = left;
	for (i = left; i < right; i++) {
		if (xs[i] <= pivot) {
			SWAP(xs[i], xs[pivotIndex]);
			pivotIndex++;
		}
	}
	SWAP(xs[pivotIndex], xs[right]);
	return pivotIndex;
}

void quicksort(int* xs, int left, int right) {
	if (left < right) {
		int middle = (left + right) / 2;
		int pivotIndex = partition(xs, left, right, middle);
		quicksort(xs, left, pivotIndex - 1);
		quicksort(xs, pivotIndex + 1, right);
	}
}

static PyObject*
quick_quicksort(PyObject* self, PyObject* args) {

	PyObject* listObj;
	int size;
	int i;

	// parse arguments

	if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &listObj))
		return NULL;

	size = PyList_Size(listObj);
	if (size < 0) return NULL;

	// convert to C array

	int list[size];

	for (i = 0; i < size; i++) {
		PyObject* itemObj = PyList_GetItem(listObj, i);
		int item = PyInt_AsLong(itemObj);
		if (item == -1 && PyErr_Occurred()) {
			return NULL;
		}
		list[i] = item;
	}

	// sort it

	quicksort(list, 0, size - 1);

	// convert back to Python list

	PyObject* newList;
	newList = PyList_New(size);
	Py_INCREF(newList);

	for (i = 0; i < size; i++) {
		PyObject* itemObj = Py_BuildValue("i", list[i]);
		PyList_SET_ITEM(newList, i, itemObj);
	}

	return newList;
}

static PyMethodDef QuickMethods[] = {
	{"quicksort", quick_quicksort, METH_VARARGS, "Sort a list of integers."},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initquick(void)
{
	(void) Py_InitModule("quick", QuickMethods);
}

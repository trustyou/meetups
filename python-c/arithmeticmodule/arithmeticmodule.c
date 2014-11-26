#include <Python.h>

static PyObject*
arithmetic_add(PyObject* self, PyObject* args)
{
	int i, j;
	PyObject* sum = NULL;
	if (!PyArg_ParseTuple(args, "ii", &i, &j))
		goto error;
	sum = PyInt_FromLong(i + j);
	if (sum == NULL)
		goto error;
	return sum;
error:
	Py_XDECREF(sum);
	return NULL;
}

static PyMethodDef ArithmeticMethods[] = {
	{"add", arithmetic_add, METH_VARARGS, "Add two integers."},
	{NULL, NULL, 0, NULL} // sentinel
};

PyMODINIT_FUNC
initarithmetic(void)
{
	(void) Py_InitModule("arithmetic", ArithmeticMethods);
}

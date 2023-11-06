#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_list_info - print info about python list
 * @p: pointer to python list
 */
void print_python_list_info(PyObject *p)
{
	int idx;

	printf("[*] Size of a Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (idx = 0; idx < Py_SIZE(p); idx++)
	{
		printf("Element %d: %s\n", idx, Py_TYPE(PyList_GetItem(p, idx))->tp_name);
	}
}

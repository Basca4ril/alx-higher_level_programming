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
	Py_ssize size;
	Py_ssize allocated, j;
	PyObject *obj;

	allocated = ((PyListObject *)p)->allocated;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (j = 0; j < size; j++)
	{
		obj = PyList_GetItem(p, j);
		printf("Element %ld: %s\n", j, Py_TYPE(obj)->tp_name);
	}
}

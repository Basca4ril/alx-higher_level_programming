#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print info about python list
 * @p: pointer to python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize size;
	Py_ssize allc, j;
	PyObject *obj;

	allc = ((PyListObject *)p)->allc;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allc);

	for (j = 0; j < size; j++)
	{
		obj = PyList_GetItem(p, j);
		printf("Element %ld: %s\n", j, Py_TYPE(obj)->tp_name);
	}
}

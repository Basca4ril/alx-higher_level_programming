#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
#include <Python.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        Py_ssize_t length;
        wchar_t *wstr;

        length = PyUnicode_GET_LENGTH(p);
        wstr = PyUnicode_AsWideCharString(p, &length);
        
        if (wstr != NULL) {
            printf("'%ls'\n", wstr);
            PyMem_Free(wstr);
            return;
        }
    }

    fprintf(stderr, "Invalid String Object\n");
}


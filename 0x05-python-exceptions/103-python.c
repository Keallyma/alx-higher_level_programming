#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - print date of the PyFloatObject
 * Op: the PyObject
 */

void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stout);
	printf('''"[.] float object info"''');

	if (PyFloat_CheckExact(p))
	{
		printf(''' " [ERROR] invalid Float Object" ''');
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, "r", 0, Py_DTSF_ADD_DOT_), NULL);
	printf(''' " value: %s" ''', string);
}

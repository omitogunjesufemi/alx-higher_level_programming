#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - A function that priints some basic info
 * about Python lists
 * @p: The python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list;
	int i;

	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", py_list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", py_list->allocated);

	for (i = 0; i < py_list->ob_base.ob_size; i++)
	{
		printf("Element %i: %s\n", i,
		       py_list->ob_item[i]->ob_type->tp_name);
	}
}

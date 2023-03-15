#include "Python.h"
#include <stdio.h>

void print_python_list(PyObject *p)
{
	PyListObject *pp;
	int i;

	pp = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n",
	       pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		printf("Element %i: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *pp;

	pp = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	printf("size: %ld\n", pp->ob_base.ob_size);
	printf("trying string: %s\n", pp->ob_sval);
	printf("first %ld bytes: %ld\n", pp->ob_base.ob_size + 1, pp->);
}

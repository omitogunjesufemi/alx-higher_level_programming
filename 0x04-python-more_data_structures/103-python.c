#include "Python.h"
#include <stdio.h>

Py_buffer *get_python_bytes(PyObject *p);
void print_python_bytes(PyObject *p);

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
		if (PyBytes_Check(pp->ob_item[i]))
			print_python_bytes(pp->ob_item[i]);

	}
}

Py_buffer *get_python_bytes(PyObject *p)
{
	Py_buffer buffer;
	Py_buffer *view;

	if (PyObject_GetBuffer(p, &buffer, PyBUF_SIMPLE) == 0)
	{
		view = &buffer;
		return (view);
	}
	return (NULL);
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *pp;
	Py_buffer *view;
	int i, n;

	if (PyBytes_Check(p))
	{
		pp = (PyBytesObject *)p;
		view = get_python_bytes(p);
		if (view->len < 10)
			n = view->len;
		else
			n = 9;
		printf("[.] bytes object info\n");
		printf("  size: %ld\n", pp->ob_base.ob_size);
		printf("  trying string: %s\n", pp->ob_sval);
		printf("  first %d bytes: ", n + 1);

		for (i = 0; i <= n; i++)
		{
			printf("%02x", ((unsigned char *)view->buf)[i]);
			if (i < n)
				printf(" ");
			else
				printf("\n");
		}
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [EROOR] Invalid Bytes Object\n");
	}
}

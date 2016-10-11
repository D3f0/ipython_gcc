Ipython GCC integration
=======================

This IPython extensions provides an easy interface to work with C code.

Installation
------------

Example usage
-------------

Define a gcc cell
~~~~~~~~~~~~~~~~~

.. code:: python


    # Example cell
    %%gcc main.c

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char **argv) {
        printf("Hello world\n");
        return 0
    }

TODO
====
View [current issues](https://github.com/D3f0/ipython_gcc/issues)

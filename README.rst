Ipython GCC integration
=======================

This IPython extensions provides an easy interface to work with C code.

Installation
------------

If you are in a terminal, just call::

    pip install -e "git+https://github.com/D3f0/ipython_gcc.git"


If already inside IPython/Jupyter:

    !pip install -e "git+https://github.com/D3f0/ipython_gcc.git"



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

View current issues_

.. _issues: https://github.com/D3f0/ipython_gcc/issues

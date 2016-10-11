"""
Interaction with GCC error output
"""
import re

regex = re.compile(r'(?P<fname>[\w\d\]\.c):(?P<line>\d+):(?P<col>\d+)')

def find_errors(output):
    return regex.finditer(output)



def test_errors():
    example_output = '''
    main.c:10:1: warning: control reaches end of non-void function [-Wreturn-type] }\
     ^ main.c:13:1: warning: type specifier missing, defaults to \
     'int' [-Wimplicit-int] float64[381][381] a,b, c; ^ \
     main.c:13:18: error: expected ';' after top level declarator float64[381][381] a,b, c; ^ ; main.c:20:44: warning: cast to 'void *' from smaller integer type 'int' [-Wint-to-void-pointer-cast] pthread_create(&hilos[i], NULL, f, (void *)i); ^ 3 warnings and 1 error generated.

    '''
    errors = find_errors(example_output)
    assert errors == []


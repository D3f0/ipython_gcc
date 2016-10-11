# coding: utf-8
"""
This IPython enables C development from a cell.
It automatically calls the compiler and generates a callable object.
It's tarteget toward concurrency and libc/OS API demos.
"""
import os
from IPython.core.magic import (
    Magics,
    magics_class,
    cell_magic,
    line_magic,
    needs_local_scope
)
try:
    from traitlets.config.configurable import Configurable
    from traitlets import Bool, Unicode, List
except ImportError:
    from IPython.config.configurable import Configurable
    from IPython.utils.traitlets import Bool, Unicode, List


from IPython.display import display, HTML
import codecs
from subprocess import Popen, PIPE

from .output import ExecutableRunner

# TODO i18n
_ = lambda x: x

@magics_class
class CompileMagic(Magics, Configurable):
    compiler = Unicode('gcc', config=True, help="Compiler to use")
    auto_add_headers = Bool(False, config=True, help="Automatically add header files")
    auto_add_flags = Bool(False, config=True, help="Automatically add compiler flags (based on headers)")
    comp_flags = List(default_value=[], config=True, help="Flags to be used at compilation")

    def __init__(self, shell):

        Configurable.__init__(self, config=shell.config)
        Magics.__init__(self, shell=shell)

        # Add ourself to the list of module configurable via %config
        self.shell.configurables.append(self)
        self.shell.ex('from gcc import ExecutableRunner')

    @needs_local_scope
    @cell_magic('gcc')
    def compile_(self, line, cell='', local_ns={}):

        name = self.extract_name(line)
        if cell:
            self.write_file(cell, name)
        target = self.get_target(name)
        if self.run_compiler(name, target):
            retval = ExecutableRunner(target)
            # Hacky way to add this element into the current NS

            code = '{0} = ExecutableRunner("./{0}")'.format(target)
            #display(HTML("<pre>%s</pre>" % code))
            self.shell.ex(code)
            #print(_("You can now access to the executable with {0} object. i.e.: {0}"
            #        ".run()".format(name)))
            return retval

    def get_target(slef, name):
        """Converts c file name into the binary"""
        return name.replace('.c', '')

    def extract_name(self, line):
        name = line.split(' ')[0]
        if not name:
            raise ValueError("Magic must be called with a filename as first arguement")
        if not name.endswith('.c'):
            name += '.c'
        return name

    def write_file(self, contents, name, encoding='utf-8'):
        if os.path.exists(name):
            action = "Overwrited"
        else:
            action = "Wrote"

        with codecs.open(name, mode='w', encoding=encoding) as fp:
            fp.write(contents)
        print("{} {}".format(action, name))

    def run_compiler(self, name, target, *flags):
        cmd_list = [self.compiler, name, '-o', target, ]
        cmd_list.extend(flags)
        cmd = ' '.join(cmd_list)
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        result = proc.wait()
        print(result)
        stdout = proc.stdout.read()
        if stdout.strip():
            print("out:")
            print('<a href="#">%s</a>' % stdout)

        stderr = proc.stderr.read()
        if stderr.strip():
            print("err")
            display(HTML('<a href="#">%s</a>' % stderr))
        return result == 0

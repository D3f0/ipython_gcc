from subprocess import Popen, PIPE
from contextlib import contextmanager
from copy import copy # Shallow copy


@contextmanager
def run_process(command, *args, **kwargs):
    p = Popen(command, *args, **kwargs)
    retval = p.wait()
    yield retval, p


class ExecutableRunner(object):
    """\
    User facing API for running binaries created with %%gcc cell magic
    """
    def __init__(self, name):
        self.name = name

    def run(self, *args, **kwargs):
        """
        Execute command
        """
        cmd = [self.name, ]
        # TODO: Detect list, tuples or iterables to run many times

        cmd.extend(map(str, args))
        with run_process(cmd, stdout=PIPE, stderr=PIPE) as (res, proc):
            # print result
            stdout = proc.stdout.read()
            if stdout.strip():
                print(stdout)

            stderr = proc.stderr.read()
            if stderr.strip():
                print(stderr)
        # TODO: View if it's better to return self for chaining
        return res

    def time(self):
        """\
        Run time statistics
        """
        with run_process('time {}'.format(self.name),
                         shell=True,
                         stdout=PIPE, stderr=PIPE) as (r, proc):
            print (proc.stderr.read().strip())
            print (proc.stdout.read().strip())

    def __str__(self):
        return './{}'.format(self.name)

    __repr__ = __str__

    def env(self, *args, **kwargs):
        """
        obj.env(PATH='/home')
        """
        if args:
            raise KeyError("Should only be used with env(ENV=val)")
        with_env = copy(self)
        with_env.env.update(**kwargs)
        return with_env

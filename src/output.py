from subprocess import Popen, PIPE


class ExecutableRunner(object):
    """\
    User facing API for running binaries created with %%gcc cell magic
    """
    def __init__(self, name):
        self.name = name

    def run(self, *args):
        cmd = [self.name, ]
        cmd.extend(map(str, args))
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=False)
        result = proc.wait()
        # print result
        stdout = proc.stdout.read()
        if stdout.strip():
            print(stdout)

        stderr = proc.stderr.read()
        if stderr.strip():
            print(stderr)
        # TODO: View if it's better to return self for chaining
        return result

    def __str__(self):
        return './{}'.format(self.name)

    __repr__ = __str__

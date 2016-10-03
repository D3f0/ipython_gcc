from magic import CompileMagic
from .output import ExecutableRunner

def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(CompileMagic)

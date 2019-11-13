"""

Add mypy type-checking cell magic to jupyter/ipython.

Save this script to your ipython profile's startup directory.

```bash
source <virtualenv>
ipython locate
```
"""

from IPython.core.magic import register_cell_magic
from IPython import get_ipython
from mypy import api


@register_cell_magic
def typecheck(line, cell):
    """
    Run the following cell though mypy.

    Any parameters that would normally be passed to the mypy cli
    can be passed on the first line, with the exception of the
    -c flag.

     i.e.

    %%typecheck --ignore-missing-imports

    mypy stdout and stderr will print prior to output of cell.
    """

    cell = '\n' + cell

    mypy_out = api.run(['-c', cell] + line.split())

    if mypy_out[0]:
        print(mypy_out[0])

    if mypy_out[1]:
        print(mypy_out[1])

    shell = get_ipython()
    shell.run_cell(cell)

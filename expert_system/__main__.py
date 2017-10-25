import sys
import fact
from file import *
from rule import *
from fact import *
from tree import *
from resolver import *

class Main:

    _file = File(sys.argv[1])
    _facts = list()

    def __init__(self):
        self._check_params()
        self._file.tree.addOpe(self._file.rules)
        res = Resolver(self._file.rules, self._file.tree, self._file.queries)
        print(self._file.tree)
        res.resolve()

    def _check_params(self):
        if len(sys.argv) > 2:
            Error("Too much arguments")
        if len(sys.argv) == 1:
            Error("Please enter a file as argument")

Main()

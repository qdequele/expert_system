import sys
import fact
from file import *
from rules import *
from fact import *
from tree import *
from resolver import *

class Main:

    _file = File(sys.argv[1])
    _facts = list()

    def __init__(self):
        self._check_params()
        print(self._file)
        res = Resolver(self._file.rules, self._file.facts, self._file.queries)
        res.resolve()

    def _check_params(self):
        if len(sys.argv) > 2:
            Error("Too mutch arguments")
        if len(sys.argv) == 1:
            Error("Please enter a file as argument")

Main()

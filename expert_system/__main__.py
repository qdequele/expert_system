import sys
import fact
from file import *
from rules import *
from fact import *
from resolver import *

class Main:

	_file = File(sys.argv[1])
	_rules = Rules()
	_facts = list()

	def __init__(self):
		self._check_params()
		for rule in self._file.getRules():
			self._rules.push(rule)
		for initial in self._file.getInitials():
			_f = Fact(initial, True)
			print(_f)
			self._facts.append(_f)
		res = Resolver(self._rules, self._facts, self._file.getQueries())
		print(str(self._facts))
		print(self._rules)

	def _check_params(self):
		if len(sys.argv) > 2:
			Error("Too mutch arguments")
		if len(sys.argv) == 1:
			Error("Please enter a file as argument")

Main()

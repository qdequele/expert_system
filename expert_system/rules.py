import re
from error import *

class Rules:

	_rules = list()

	def __init__(self):
		pass

	def __str__(self):
		return str(self._rules)

	def _check_parentheses(self, line):
		i = 0
		for c in line:
			if c == '(':
				i += 1
			elif c == ')':
				i -= 1
			if i == -1:
				return False
		return i == 0

	def push(self, line):
		if re.match("^\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+(<?=>)\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+$", line) is None\
			or self._check_parentheses(line) is False:
			Error("Error during parse rules")
		self._rules.append(line)

	def getRules(self):
		return self._rules

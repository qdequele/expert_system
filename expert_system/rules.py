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
		if re.match("^!?\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+(<?=>)!?\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+$", line) is None\
			or self._check_parentheses(line) is False:
			Error("Error during parse rules")
		rule = re.split("=>|<=>", line)
		for item, fact in rule:
			print(fact, item)
			# rule[item] = re.split("([+|^])", fact)
			# print(fact)
		self._rules.append(rule)

	def getRules(self):
		return self._rules

import re

class Rules:
    _rules = list()
    def __init__(self):
		pass

	def __str__(self):
		return str(self._rules)
	
	def _check_parenthesis(self, line):
		return True

	def push(self, line):
		if re.match("^\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+(<?=>)\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+$", line) is None
			or _check_parenthesis(line) is False:
			print("Error during parse rules")
			sys.exit(1)
		if _check_parenthesis(line) is False
		self._rules.append(line)

	def getRules(self):
		return self._rules

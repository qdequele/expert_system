import re
from error import *

class Rule:

    _rule = []

    def __init__(self, line):
        if re.match("^!?\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+(<?=>)!?\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+$", line) is None\
            or self._check_parentheses(line) is False:
            Error("Error during parse rules")
        rule = re.split("=>|<=>", line)
        for item, fact in enumerate(rule):
            rule[item] = self._formating(fact)
        self._rule = rule

    def __str__(self):
        return str(self._rule)

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return self._rule[key]

    def __len__(self):
        return len(self._rule)

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

    def _formating(self, ope):
        match = re.match("^(\(.*\)|.*)([+^|])(\(.*\)|.*)$", ope)
        if match is not None:
            data = match.groups()	
            ope = list()
            ope.append(self._formating(data[0]))
            ope.append(data[1])
            ope.append(self._formating(data[2]))
        return ope

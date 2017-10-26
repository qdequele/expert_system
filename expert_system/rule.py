import re
from error import *

class Rule:

    def __init__(self, line):
        if re.match("^!?\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+(=>)!?\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+$", line) is None\
            or self._check_parentheses(line) is False:
            Error("Error during parse rules")
        operation = re.split("=>", line)
        for item, fact in enumerate(operation):
            operation[item] = self._formating(fact)
        self.rule = operation

    def __str__(self):
        return str(self.rule)

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return self.rule[key]

    def __len__(self):
        return len(self.rule)

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
        matchXor = re.match(r"^((\))?.*(\))?)(\^)((\))?.*(\))?)$", ope)
        matchAnd = re.match(r"^((\))?.*(\))?)(\+)((\))?.*(\))?)$", ope)
        matchOr = re.match(r"^((\))?.*(\))?)(\|)((\))?.*(\))?)$", ope)
        # print("formating : %s"%(ope))
        if matchOr is not None:
            ope = self._match(filter( None, matchOr.groups()))
        elif matchAnd is not None:
            ope = self._match(filter( None, matchAnd.groups()))
        elif matchXor is not None:
            ope = self._match(filter( None, matchXor.groups()))
        if len(ope) == 2:
            ope = ope.replace("(", "")
            ope = ope.replace(")", "")
        return ope

    def _match(self, data):
        ope = list()
        # print ("%s %s %s"%(data[0], data[1], data[2]))
        ope.append(self._formating(data[0]))
        ope.append(data[1])
        ope.append(self._formating(data[2]))
        return ope

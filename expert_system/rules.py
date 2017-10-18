import re

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
            elif c == ')'
                i -= 1
            if i == -1
                return False
        return i == 0

    def push(self, line):
        if re.match("^\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+(<?=>)\(?!?[A-Z]\)?(([+^|]\(?!?[A-Z]\)?)?)+$", line) is None
            or _check_parentheses(line) is False:
            print("Error during parse rules")
            sys.exit(1)
        self._rules.append(line)

    def getRules(self):
        return self._rules


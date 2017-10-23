from fact import *

class Resolver:

    _rules = []
    _facts = []
    _queries = []

    def __init__(self, rules, facts, queries):
        self._rules = rules
        self._facts = facts
        self._queries = queries

    def __str__(self):
        return "Rules: %s\nInitial Fatcs: %s\nQueries : %s\n"%(self._rules, self._facts, self._queries)

    def resolve(self):
        # print("resolve:")
        # print(self._rules)
        for query in self._queries:
            val = self.search(query, self._rules)
            if val is None:
                print("Impossible to answer")
            else:
                print("{} is {}".format(query, val))

    def search(self, query, rules):
        for i, rule in enumerate(rules):
            if query in rule[0]:
                self.searchInRule(query, rules, i, -1)
            elif query in rule[-1]:
                self.searchInRule(query, rules, i, 0)
            else:
                return None

    def searchInRule(self, query, rules, index, pos):
        if len(rules[index][pos]) is 1:
            value = filter(lambda x: x.letter is rules[index][pos], self._facts)[0].value
            if value is not None:
                filter(lambda x: x.letter is query, self._facts)[0].value = value
                return value
            else:
                return self.search(rules[index][pos], [rules.pop(index - 1)])
        else:
            self.solve(rules[index][pos])

    def solve(self, op):
        if len(op) is 1:
            if op[0].startswith('!'):
                return solve_not(filter(lambda x: x.letter is op[0], self._facts)[0].value)
            else:
                return filter(lambda x: x.letter is op[0], self._facts)[0].value
        elif op[1] is '|':
            return solve_or(self.solve(op[0]), self.solve(op[2]))
        elif op[1] is '+':
            return solve_and(self.solve(op[0]), self.solve(op[2]))
        elif op[1] is '^':
            return solve_xor(self.solve(op[0]), self.solve(op[2]))

    def solve_not(self, fact):
        if fact.value is not None:
            return not fact.value
        else:
            return None

    def solve_or(self, fact1, fact2):
        if fact1.value or fact2 is True:
            return True
        else:
            return False
    
    def solve_and(self, fact1, fact2):
        if fact1.value or fact2 is None:
            return None
        elif fact1.value and fact2 is True:
            return True
        else:
            return False

    def solve_xor(self, fact1, fact2):
        if fact1.value or fact2 is None:
            return None
        elif fact1.value is fact2.value:
            return False
        else:
            return True
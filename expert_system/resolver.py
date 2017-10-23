from fact import *
from error import *

class Resolver:

    _rules = []
    _facts = {}
    _queries = []

    def __init__(self, rules, facts, queries):
        self._rules = rules
        self._facts = facts
        self._queries = queries

    def __str__(self):
        return "Rules: %s\nInitial Fatcs: %s\nQueries : %s\n"%(self._rules, self._facts, self._queries)

    def resolve(self):
        print("resolve : %s"%(self._queries))
        for query in self._queries:
            val = self.search(query, self._rules)
            if val is None:
                Error("Impossible to answer")
            else:
                print("{} is {}".format(query, val))

    def search(self, query, rules):
        for i, rule in enumerate(rules):
            print("search %s in rule: %s"%(query, rule))
            if query in rule[0]:
                return self.searchInRule(query, rules, i, -1)
            elif query in rule[-1]:
                return self.searchInRule(query, rules, i, 0)
            else:
                pass

    def searchInRule(self, query, rules, index, pos):
        print("searchInRule: %s"%(rules[index][pos]))
        if len(rules[index][pos]) is 1:
            value = self._facts[rules[index][pos]]
            if value is not None:
                print("searchInRule value: %s"%(value))
                return value
            else:
                print("searchInRule value is none")
                return self.search(rules[index][pos], [rules.pop(index - 1)])
        else:
            print("searchInRule need to solve new operation")
            return self.solve(rules[index][pos])

    def solve(self, op):
        if len(op) is 1:
            if op[0].startswith('!'):
                return self.solve_not(op[0])
            else:
                return self._facts[op[0]]
        elif op[1] is '|':
            return self.solve_or(self.solve(op[0]), self.solve(op[2]))
        elif op[1] is '+':
            return self.solve_and(self.solve(op[0]), self.solve(op[2]))
        elif op[1] is '^':
            return self.solve_xor(self.solve(op[0]), self.solve(op[2]))

    def solve_not(self, fact):
        if fact is not None:
            return not fact.value
        else:
            return None

    def solve_or(self, fact1, fact2):
        if fact1 is True or fact2 is True:
            print("fact1: %s | fact2: %s -> True"%(fact1, fact2))
            return True
        else:
            print("fact1: %s | fact2: %s -> False"%(fact1, fact2))
            return False
    
    def solve_and(self, fact1, fact2):
        if fact1 is None or fact2 is None:
            print("fact1: %s + fact2: %s -> None"%(fact1, fact2))
            return None
        elif fact1 is True and fact2 is True:
            print("fact1: %s + fact2: %s -> True"%(fact1, fact2))
            return True
        else:
            print("fact1: %s + fact2: %s -> False"%(fact1, fact2))
            return False

    def solve_xor(self, fact1, fact2):
        if fact1 is None or fact2 is None:
            print("fact1: %s ^ fact2: %s -> None"%(fact1, fact2))
            return None
        elif fact1 is fact2:
            print("fact1: %s ^ fact2: %s -> False"%(fact1, fact2))
            return False
        else:
            print("fact1: %s ^ fact2: %s -> True"%(fact1, fact2))
            return True

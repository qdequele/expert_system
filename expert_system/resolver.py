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
        # print("----search")
        # print("search : " + query)
        # print("rules {}".format(rules))
        for i, rule in enumerate(rules):
            if query in rule[0]:
                if len(rule[-1]) is 1:
                    value = filter(lambda x: x.letter is rule[-1], self._facts)[0].value
                    if value is not None:
                        filter(lambda x: x.letter is query, self._facts)[0].value = value
                        return value
                    else:
                        return self.search(rule[-1], [rules.pop(i - 1)])
                else:
                    # decompose
                    pass
            elif query in rule[-1]:
                if len(rule[0]) is 1:
                    value = filter(lambda x: x.letter is rule[0], self._facts)[0].value
                    if value is not None:
                        filter(lambda x: x.letter is query, self._facts)[0].value = value
                        return value
                    else:
                        return self.search(rule[0], [rules.pop(i - 1)])
                else:
                    # decompose
                    pass
            else:
                return None
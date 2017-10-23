from fact import *

class Resolver:

    def __init__(self, rules, tree, queries):
        self._rules = rules
        self._tree = tree
        self._queries = queries

    def __str__(self):
        return "Rules: %s\nInitial Tree: %s\nQueries : %s\n"%(self._rules, self._tree, self._queries)

    def resolve(self):
        for query in self._queries:
            print("%s = %s"%(query, self._tree.get(query).solve()))

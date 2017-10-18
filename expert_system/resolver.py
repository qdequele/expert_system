class Resolver:

	_rules = list()
	_facts = list()
	_queries = list()

	def __init__(self, rules, facts, queries):
		self._rules = rules
		self.facts = facts
		self.queries = queries

	def __str__(self):
		return "Rules: %s\nInitial Fatcs: %s\nQueries : %s\n"%(self._rules, self._initial, self._queries)

	def resolve():
		pass

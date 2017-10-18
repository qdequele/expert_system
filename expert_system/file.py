import itertools
import sys
from error import *

class File:

	_rules = []
	_initial = []
	_queries = []

	def __init__(self, filename):
		try:
			file = open(filename)
		except IOError:
			Error("Open file failed")
		text = file.readlines()
		for i, _ in enumerate(text):
			text[i] = text[i].translate(None, '\t\n')
			text[i], _, _ = text[i].partition('#')
			text[i] = text[i].strip()
			if len(text[i]) == 0:
				text[i] = None
			pass
		text = filter(None, text)
		self._initial = filter(None, ''.join(ch for ch, _ in itertools.groupby(
			filter(lambda x: x.startswith('?'), text)))
			.translate(None, ' ?'))
		self._queries = filter(None, ''.join(ch for ch, _ in itertools.groupby(
			filter(lambda x: x.startswith('='), text)))
			.translate(None, ' ='))
		self._rules = filter(lambda x: not x.startswith('='),
			filter(lambda x: not x.startswith('?'), text))
		if len(self._initial) == 0:
			Error("Imposible to resolve, please add initial facts")
		if len(self._queries) == 0:
			Error("No queries found, please add a querie at the end of the file")
		if len(self._rules) == 0:
			Error("No rules found, please add rules")

	def __str__(self):
		return "Rules: %s\nInitial Fatcs: %s\nQueries : %s\n"%(self._rules, self._initial, self._queries)

	def getRules(self):
		return self._rules

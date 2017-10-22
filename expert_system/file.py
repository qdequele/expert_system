import itertools
import sys
from error import *
from fact import *
from rule import *
class File:

    rules = []
    queries = []
    facts = []

    def __init__(self, filename):
        try:
            file = open(filename)
        except IOError:
            Error("Open file failed")
        text = file.readlines()
        for i, _ in enumerate(text):
            text[i] = text[i].translate(None, '\t\n ')
            text[i], _, _ = text[i].partition('#')
            text[i] = text[i].strip()
            if len(text[i]) == 0:
                text[i] = None
            pass
        text = filter(None, text)
        initial = filter(None, ''.join(ch for ch, _ in itertools.groupby(
            filter(lambda x: x.startswith('?'), text)))
            .translate(None, ' ?'))
        facts = filter(None, set(''.join(text).translate(None, ' ?=()>+^|!')))
        for fact in facts:
            if fact in initial:
                self.facts.append(Fact(fact, True))
            else:
                self.facts.append(Fact(fact))
        self.queries = filter(None, ''.join(ch for ch, _ in itertools.groupby(
            filter(lambda x: x.startswith('='), text)))
            .translate(None, ' ='))
        self.rules = map(lambda x: Rule(x), filter(lambda x: not x.startswith('='),
            filter(lambda x: not x.startswith('?'), text)))
        if len(initial) == 0:
            Error("Imposible to resolve, please add initial facts")
        if len(self.queries) == 0:
            Error("No queries found, please add a querie at the end of the file")
        if len(self.rules) == 0:
            Error("No rules found, please add rules")

    def __str__(self):
        return "Rules: %s\nInitial Fatcs: %s\nQueries : %s\n"%(self.rules, self.facts, self.queries)
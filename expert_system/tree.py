from node import *

class Tree:

    def __init__(self):
        self.tree = {}

    def __str__(self):
        string = "{\n"
        for letter in self.tree:
            string += "%s\n"%(str(self.tree[letter]))
        string += "}"
        return string

    def append(self, letter, fact):
        if letter not in self.tree:
            self.tree[letter] = fact
            return True
        return False

    def get(self, letter):
        return self.tree[letter]

    def _add(self, letter, ope):
        if isinstance(letter, list):
            self.tree[letter[1]].ope.append(Node(operator='!', left=ope))
        else:
            self.tree[letter].ope.append(ope)

    def _searchFact(self, ope):
        if isinstance(ope, str):
            return self.tree[ope]
        res = [None]*len(ope)
        for index, elem in enumerate(ope):
            if isinstance(elem, list):
                res[index] = self._searchFact(elem)
            elif elem.isalpha():
                res[index] = self.tree[elem]
            else:
                res[index] = elem
        if len(res) is 2:
            res = Node(operator=res[0], left=res[1])
        elif len(res) is 3:
            res = Node(left=res[0], operator=res[1], right=res[2])
        return res


    def addOpe(self, rules):
        for elem in rules:
            res = self._searchFact(elem[0])
            if len(elem[1]) == 3:
                self._add(elem[1][0], res)
                self._add(elem[1][-1], res)
            else:
                self._add(elem[1], res)
                

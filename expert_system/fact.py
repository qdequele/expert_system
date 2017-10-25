import sys

class Fact:

    type = "fact"

    def __init__(self, letter, value = None):
        self.value = value
        self.letter = letter
        self.ope =[]

    def __str__(self):
        string = "%s: %s, ope :"%(self.letter, self.value)
        if len(self.ope) is 0:
            string += "[]"
        for elem in self.ope:
            string += "\n\t%s"%(elem)
        return string

    def val(self):
        val = self.solve()
        return val if val is not None else False

    def solve(self):
        ret = []
        for node in self.ope:
            ret.append(node.solve())
        if ret.count(True) and ret.count(False):
            print("Incompatible operations")
            sys.exit(0)
        value = True if ret.count(True) else False if ret.count(False) else None
        if self.value is not None and value is not None and self.value is not value:
            print("Difference between initial and calculate value")
            sys.exit(0)
        self.value = value if value is not None else self.value
        return self.value


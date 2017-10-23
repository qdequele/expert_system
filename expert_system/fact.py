import sys

class Fact:

    type = "fact"

    def __init__(self, letter, value = None):
        self.value = value
        self.letter = letter
        self.ope =[]

    def __str__(self):
        return "{%s : %s, ope : %s}"%(self.letter, self.value, self.ope)

    def val(self):
        return self.value

    def solve(self):
        ret = []
        for node in self.ope:
            ret.append(node.solve())
        if ret.count(True) and ret.count(False) :
            print("Incompatible operations")
            sys.exit(0)
        value = True if ret.count(True) else False if ret.count(False) else None
        if self.value is not None and value is not None and self.value <> value:
            print("Difference between initial and calculate value")
            sys.exit(0)
        self.value = value if value is not None else self.value
        return self.value


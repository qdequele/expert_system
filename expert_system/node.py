import sys

class Node:

    functions = {
        '|': 'solve_or',
        '+': 'solve_and',
        '^': 'solve_xor',
        '!': 'solve_not'
    }

    def __init__(self, left, operator, right=None):
        self.left = left
        self.right = right
        self.operator = operator
        try:
            self.solve = getattr(self, Node.functions[operator])
        except Exception as e:
            print(e)
            sys.exit(e)

    def __str__(self):
        if self.right is None:
            return "%s %s = %s"%(self.operator, self.left.val(), self.solve())
        else:
            return "%s %s %s = %s"%(self.left.val(), self.operator, self.right.val(), self.solve())
            

    def val(self):
        return self.solve()

    def solve_not(self):
        if self.left.val() is not None:
            return not self.left.val()
        else:
            return None

    def solve_or(self):
        if self.left.val() is True or self.right.val() is True:
            return True
        elif self.left.val() is None or self.right.val() is None:
            return None
        else:
            return False
    
    def solve_and(self):
        if self.left.val() is True and self.right.val() is True:
            return True
        elif self.left.val() is None or self.right.val() is None:
            return None
        else:
            return False

    def solve_xor(self):
        if self.left.val() is None or self.right.val() is None:
            return None
        elif self.left.val() is self.right.val():
            return False
        else:
            return True

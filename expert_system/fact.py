
class Fact:

    # value = None
    # ope = []

    def __init__(self, value = None):
        self.value = value
        self.ope =[]

    def __str__(self):
        return "{value : %s, ope : %s}"%(self.value, self.ope)

    def value(self):
        return self.value

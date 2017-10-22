
class Fact:

    letter = ''
    value = None

    def __init__(self, letter, value = None):
        self.letter = letter
        self.value = value

    def __str__(self):
        return self.letter + ' = ' + str(self.value)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return ord(self.letter)

    def __eq__(self, other):
        return self.letter is other.letter

    def __ne__(self, other):
        return self.letter is not other.letter

    def __getitem__(self, key):
        if self.letter is key:
            return self.value
        else:
            return None

class Fact:
    
    def __init__(self, letter, value = None):
        self._letter = letter
        self._value = value
    
    _letter = ''
    _value = None

    def __str__(self):
        return self._letter + ' = ' + self._value

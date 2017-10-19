class Fact:

	_letter = ''
	_value = None

	def __init__(self, letter, value = None):
		self._letter = letter
		self._value = value

	def __str__(self):
		return self._letter + ' = ' + str(self._value)

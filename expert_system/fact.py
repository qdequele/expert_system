
class Fact:

	letter = ''
	value = None

	def __init__(self, letter, value = None):
		self.letter = letter
		self.value = value

	def __str__(self):
		return self.letter + ' = ' + str(self.value)

	def op_not(self):
		self.value is not self.value

	def op_or(self, left, right):
		if left.value is True or right.value is True
			self.value = True
		elif left.value is False and right.value is False:
			self.value = False
		elif :
			self.value = None

	def op_and(self, left, right):
		if left.value is True and right.value is True
			self.value = True
		elif left.value is False or right.value is False:
			self.value = False
		elif :
			self.value = None

	def op_xor(self, left, right):
		if (left.value is True or right.value is True) and not (left.value is True and right.value is True)
			self.value = True
		elif left.value is not None and right.value is not None:
			self.value = False
		elif :
			self.value = None

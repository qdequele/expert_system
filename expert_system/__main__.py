import sys
import rules

def check_params():
	if len(sys.argv) > 2:
		print("Too mutch arguments")
		sys.exit(1)
	if len(sys.argv) == 1:
		print("Please enter a file as argument")
		sys.exit(1)

def parse_file():
	try:
		file = open(sys.argv[1])
	except IOError:
		print("Open file failed")
		sys.exit(1)
	text = file.readlines()
	for i, _ in enumerate(text):
		text[i] = text[i].translate(None, '\t\n')
		text[i], _, _ = text[i].partition('#')
		text[i] = text[i].strip()
		if len(text[i]) == 0:
			text[i] = None
		pass
	text = filter(None, text)
	return text

def get_values(text):
	print(text)
	questions = filter(lambda x: x.startswith('?'), text)
	print(questions)
	affirmations = filter(lambda x: x.startswith('='), text)
	print(affirmations)

check_params()
text = parse_file()
get_values(text)

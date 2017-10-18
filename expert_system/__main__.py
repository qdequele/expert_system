import sys

def check_params():
	if len(sys.argv) > 2:
		print("Too mutch arguments")
		sys.exit(1)
	if len(sys.argv) == 1:
		print("Please enter a file as argument")
		sys.exit(1)

def parse_file():
	file = open(sys.argv[1])
	text = file.readlines()
	for i, _ in enumerate(text):
		text[i] = text[i].translate(None, '\t\n')
		text[i], _, _ = text[i].partition('#')
		text[i] = text[i].strip()
		if len(text[i]) == 0:
			text[i] = None
		pass
	text = filter(None, text)
	print(text)

check_params()
parse_file()

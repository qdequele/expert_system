import sys
import fact
from file import *

def check_params():
	if len(sys.argv) > 2:
		Error("Too mutch arguments")
	if len(sys.argv) == 1:
		Error("Please enter a file as argument")

check_params()
file = File(sys.argv[1])

# for rule in file.getRules():
print(file)

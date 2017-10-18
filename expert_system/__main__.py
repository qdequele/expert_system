import sys
import fact
from file import *

def check_params():
	if len(sys.argv) > 2:
		print("Too mutch arguments")
		sys.exit(1)
	if len(sys.argv) == 1:
		print("Please enter a file as argument")
		sys.exit(1)

check_params()
file = File(sys.argv[1])
print(file)

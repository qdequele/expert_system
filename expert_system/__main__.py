import sys
import fact
from file import *
from rules import *
from fact import *

def check_params():
	if len(sys.argv) > 2:
		Error("Too mutch arguments")
	if len(sys.argv) == 1:
		Error("Please enter a file as argument")

check_params()
file = File(sys.argv[1])
rules = Rules()
fact = list()

for rule in file.getRules():
	rules.push(rule)

for initial in file.getInitials():
	fact.append(Fact(initial, True))

print(fact)

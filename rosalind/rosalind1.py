#!/usr/bin/python3
#input must consist of two numeric values

from sys import argv

#test that input is correct
assert len(argv) == 3, "Incorrect input - should consist of two numerical values"
assert argv[1].isnumeric(), "Incorrect input - ensure only numeric values provided"

hypot = 0

#loop through the input numbers, square them and add them together
for i in argv[1:]:
	hypot += (int(i) ** 2)

print(hypot)


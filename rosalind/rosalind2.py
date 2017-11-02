#!/usr/bin/python3

from sys import argv

adenines = 0
guanines = 0
cytosines = 0
thymines = 0

sequence = argv[1]

for i in range(0, len(sequence)):
	if sequence[i] == 'A': adenines += 1
	if sequence[i] == 'C': cytosines += 1
	if sequence[i] == 'T': thymines += 1
	if sequence[i] == 'G': guanines += 1

print(adenines,cytosines, guanines, thymines)
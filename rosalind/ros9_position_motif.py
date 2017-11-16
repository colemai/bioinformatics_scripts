#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find each position of a given single motif in a given single sequence
Input: Text file, first line contains string, second contains motif
Output: each input position, as int on one line separated by a space
"""

from sys import argv

#Step1: Import string and motif
def parse_input (input):
	"""
	Input: text file, first line contains string, second contains motif
	Output: list with first elem as sequence str, second elem as motif str
	"""
	with open(input) as file_object:
		lines = file_object.readlines()
		#Assertion here
		sequence = lines[0].strip()
		motif = lines[1].strip()
	return [sequence, motif]

#Step2: List each starting position of motif in string
def find_motif_locations (motif, sequence):
	"""
	Input: Motif, sequence each as strings
	Output: List of positions of motif (position by the genetic way which is +1 of python)
	"""
	index = 0
	motif_positions = []
	while index != -1:
		index = sequence.find(motif, index + 1) 
		if index != -1: motif_positions.append(index + 1)
	return(motif_positions)

#Step3: Assertions
#Assert that motif is in string
#Assert that motif and string are given and that type is correct
#Assert that motif is not longer than string

#Step4: Run functions
if __name__ == "__main__":
	motif_and_sequence = parse_input(argv[1])
	motif_positions = find_motif_locations(motif_and_sequence[1], motif_and_sequence[0])
	for item in motif_positions:
		print(item, end=" ")





#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Text file, first line contains n symbols (n <= 10), second line contains 
an int (n)
Output: Multiple strings each printed on their own line (all strings that can be 
formed from the symbols of length n)
Example call: python3 ros25-lexf.py input.txt
"""

from sys import argv
import pdb
import itertools

def import_alphabet_n (file_path):
	"""
	Input: Text file, first line contains n symbols (n <= 10), second line 
	contains an int
	Output: List (alphabet of symbols), int (n)
	"""
	with open(file_path) as file_object:
		lines = file_object.readlines()
		alphabet = lines[0].strip().split(' ')
		n = int(lines[1])
	return alphabet, n

def get_all_words (alphabet, n):
	"""
	Input: List --> alphabet of symbols, Int --> n
	Output: List --> all strings of length n from the given alphabet, in 
	alphabetical order
	"""
	# Create n copies of the alphabet...to later combine into strings
	vectors = []
	for i in range(0,n):
		vectors.append(alphabet)

	# Combine the n vectors in each way possible, as tuples
	word_tuples = []
	for t in itertools.product(*vectors):
		word_tuples.append(t)

	# Convert the tuples to strings and return them
	joiner = ''.join
	return list(map(joiner, word_tuples))


if __name__ == "__main__":
	alphabet, n = import_alphabet_n(argv[1])
	all_words = get_all_words(alphabet, n)

	# Print in the required format, one line per string
	for perm in all_words:
		seq = ''
		for number in perm:
			seq += str(number)
		print(seq)

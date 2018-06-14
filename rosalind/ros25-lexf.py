#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Text file, first line contains n symbols (n <= 10), second line contains 
an int
Output: Multiple strings each printed on their own line (all strings that can be 
formed from the symbols)
Example call: python3 ros25-lexf.py input.txt
"""

from sys import argv
import pdb

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



if __name__ == "__main__":
	alphabet, n = import_alphabet_n(argv[1])
	print(alphabet,n)

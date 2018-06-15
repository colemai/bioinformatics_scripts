#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Text file with an int (n) on the first line, a permutation of length n
on the second line
Output: The longest possible increasing subsequence followed by the decreasing
Example Call: python3 ros26-lgis.py input.txt
"""

from sys import argv
import pdb

def import_n_perm (file_path):
	"""
	Input: Text file, first line contains an int (n), second line 
	contains a permutation of length n
	Output: int (n), List (alphabet of symbols)
	"""
	with open(file_path) as file_object:
		lines = file_object.readlines()
		perm = lines[1].strip().split(' ')
		perm = [ int(x) for x in perm ]
		n = int(lines[0])
	return n, perm


if __name__ == "__main__":
	n, perm = import_n_perm(argv[1])
	print(n, perm)
#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find partial permutations as per http://rosalind.info/problems/pper/
Input: Path to txt file, two ints on one line separated by a space
Output: Int
"""

from sys import argv
import pdb
import math

def get_ints_from_file (file_path):
	"""
	Returns two ints from txt file with two ints on one line
	"""
	with open(file_path) as file_object:
		line = file_object.read()
	return line.split(' ')


if __name__ == "__main__":
	n,k = get_ints_from_file(argv[1])
	
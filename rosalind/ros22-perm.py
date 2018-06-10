#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: An integer (n)
Output: The number of permutations of length n and a list of those permutations
"""

from sys import argv
import pdb
import numpy as np
import itertools
import math

from ian_bif_utilities import get_input_ints

def permutations(n):
	"""
	Input: Int n
	Output: List of all n lengthed permutations 1..n E R
	"""
	original = list(range(1,n+1))
	return list(itertools.permutations(original)) #this feels like cheating...


if __name__ == "__main__":
	n = get_input_ints(argv[1])[0] #get first and only element from input list
	perms = permutations(n)

	#Printing bit
	print(math.factorial(n))
	# for perm in perms:
	# 	print(perm)

	for perm in perms:
		seq = ''
		for number in perm:
			seq += str(number)
			seq += ' '
		print(seq)
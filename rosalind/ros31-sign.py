#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Give all signed permutations 
Input: Int (from txt file)
Output: Int (no. signed permutations), then all signed permutations
Briefing: http://rosalind.info/problems/sign/
"""

from sys import argv
import pdb
import numpy as np
import itertools
from ian_bif_utilities import get_input_ints



def permutations(n):
	"""
	Input: Int n
	Output: List of all n lengthed permutations 1..n E R
	"""
	original = list(range(1,n+1))
	return list(itertools.permutations(original))

def signed_perms (perm):
	"""
	Input: List of ints (all positive)
	Output: List of lists of ints (all combinations of pos/neg of input list)
	"""
	signed_perms = []


	return [1]




if __name__ == "__main__":
	n = get_input_ints(argv[1])[0] #get first and only element from input list
	print(n)

	perms = permutations(n)
	print(perms)

	master_list = []
	for perm in perms:
		master_list += signed_perms(perm)
	print(master_list)
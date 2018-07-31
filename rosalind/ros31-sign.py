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
from itertools import chain, combinations

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

	# Get all possible combinations of items in this permutation
	complete_combos = list(chain.from_iterable(combinations(perm, r) for r in range(len(perm)+1)))

	# For each of these combinations assign a negative sign
	for combo in complete_combos:
		this_perm = perm[:]
		for i in combo:
			this_perm[i-1] *= -1
		signed_perms.append(this_perm) # add this sign-perm to the output
	return(signed_perms)



if __name__ == "__main__":
	n = get_input_ints(argv[1])[0] #get first and only element from input list

	perms = permutations(n) # get all permutations (not signed ones)
	perms = [list(elem) for elem in perms] #Turn perms into lists from tuples

	# Get all signed perms for each perm
	master_list = []
	for perm in perms:
		master_list += signed_perms(perm)

	# Printing bit
	print(len(master_list))
	for j in master_list:
		print(*j)
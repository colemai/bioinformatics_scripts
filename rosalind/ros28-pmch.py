#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find total possible number of perfect basepair edge matchings as per
http://rosalind.info/problems/pmch/
Input: Fasta file path, single RNA seq (same no. A's as U's and G's as C's)
Output: Integer, Number of perfect matchings basepair edges of that seq
"""

from sys import argv
import pdb
import numpy as np
import itertools

from ian_bif_utilities import single_fasta_to_string


if __name__ == "__main__":
	rna_seq = single_fasta_to_string(argv[1])

	#Count the number of each base 
	#TODO A and U could be merged into one count (and obvs G/C)
	remaining_A = rna_seq.count('A')
	remaining_U = rna_seq.count('U')
	remaining_G = rna_seq.count('G')
	remaining_C = rna_seq.count('C')

	# Create value for perfect matches, to later be modified
	perf_matches = 1

	# Iterate through each base in the seq 
	# TODO it's actually only necessary to go through half the seq, incorporate.
	for i in range(0, len(rna_seq)):
		# Multiply perf_matches by the remaining number of candidate bases
		if rna_seq[i] == 'A': 
			if remaining_U != 0: #Account for multiplication by zero
				perf_matches *= remaining_U
				remaining_U -= 1 #update the base counts as they're consumed
				remaining_A -= 1
		elif rna_seq[i] == 'G': 
			if remaining_C != 0:
				perf_matches *= remaining_C
				remaining_C -= 1
				remaining_G -= 1
		elif rna_seq[i] == 'C': 
			if remaining_G != 0:
				perf_matches *= remaining_G
				remaining_G -= 1
				remaining_C -= 1
		elif rna_seq[i] == 'U': 
			if remaining_A != 0:
				perf_matches *= remaining_A
				remaining_A -= 1
				remaining_U -= 1

	print('Perfect Matches: ', perf_matches)

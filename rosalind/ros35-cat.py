#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find no. perfect matchings RNA as per 
http://rosalind.info/problems/cat/
Input: Fasta file path, one RNA seq (num A == num U, same for C-G)
Output: Int, number of perfect matchings
"""

# Standard Libs
from sys import argv
import pdb

# My Own External Funcs
from ian_bif_utilities import single_fasta_to_string

def count_noncross_perf_matches (nodes):
	"""
	Purpose: Count noncrossing perfect matches
	Input: INT nodes the number of nodes in the circular graph
	Output: INT total number of non-crossing perfect matches
	"""
	n = int(nodes/2)
	local_total = 0
	for m in range(2, nodes+1, 2):
		n_left = int((m - 2)/2)
		n_right = int((nodes - m)/2)

		# For each side of the 1-m bond, count noncross-perf-matches
		if n_left == 2:
			c_left = 2
		elif n_left == 1:
			c_left = 1
		elif n_left == 0:
			c_left = 1
		else: c_left = count_noncross_perf_matches(n_left * 2)

		if n_right == 2:
			c_right = 2 
		elif n_right == 1:
			c_right = 1 
		elif n_right == 0:
			c_right = 1 
		else: c_right = count_noncross_perf_matches(n_right * 2)
		
		local_total += c_left * c_right

	return local_total

if __name__ == "__main__":
	seq = single_fasta_to_string(argv[1])
	nodes = len(seq)
	matchings = count_noncross_perf_matches(nodes)
	print(matchings)

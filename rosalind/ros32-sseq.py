#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find subseq of DNA string accounting for gaps 
(http://rosalind.info/problems/sseq/)
Input: Fasta file with two DNA strings
Output: Ints (indices of second DNA string as subseq of first)
"""

import pdb
from sys import argv

from ian_bif_utilities import fasta_to_list

def find_subsequence (seq, subseq):
	"""
	Input: Two Strings, one is a subseq of the other (maybe not contiguous)
	Output: List (indices of subseq in seq)
	"""
	indices = [] # create output list

	current_index = -1 # use this as iterator to ensure correct order
	cut_length = 0 # this to account for the bits I cut off in iterating
	# iterate through the letters in subseq, find first occurence in seq
	for base in subseq:
		current_index = seq[current_index + 1:].find(base) + cut_length 
		indices.append(current_index)
		cut_length = current_index + 1
	
	indices = [i + 1 for i in indices] # they don't want zero-indexed
	return(indices)


if __name__ == "__main__":
	seq_t, seq_s = fasta_to_list(argv[1])

	indices = find_subsequence(seq_t, seq_s)
	print(*indices)
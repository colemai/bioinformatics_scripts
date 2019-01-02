#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Suggest corrections for sequence reads as per 
http://rosalind.info/problems/corr/
Input: Fasta file path, up to 1000 DNA reads of up to 50bp
Output: Printed Strings, multiple lines of 'wrong seq' --> 'correct seq'
"""

# Standard Libs
from sys import argv
import pdb

from ian_bif_utilities import fasta_to_list, generate_reverse_complement_dna





if __name__ == "__main__":
	seqs = fasta_to_list(argv[1])
	print(seqs)

	# Get all correct sequences
	# Create a set of correct seqs then add all their revcomps

	correct_sequences = []
	temp_seqs = seqs[:] # as I'll be removing elements
	for sequence in seqs:
		temp_seqs.remove(sequence)
		# pdb.set_trace()
		rev_comp = generate_reverse_complement_dna(sequence)
		if sequence in temp_seqs:
			correct_sequences.append(sequence)
		elif rev_comp in temp_seqs:
			correct_sequences.append(sequence)

	print(correct_sequences)
	# By inference, all incorrect sequences
	# Add reverse complement for each correct sequence to correct list

	# Then hard bit, iterate through incorrects and match them with a correct
	# of hamming distance 1 (will only be one apparently)
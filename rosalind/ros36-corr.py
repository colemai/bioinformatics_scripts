#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Suggest corrections for sequence reads as per 
http://rosalind.info/problems/corr/
Input: Fasta file path, up to 1000 DNA reads of up to 50bp
Output: Printed Strings, multiple lines of 'incorrect seq' --> 'correct seq'
"""

# Standard Libs
from sys import argv
import pdb

from ian_bif_utilities import fasta_to_list, generate_reverse_complement_dna


def get_hamming_dist_dna (seqs):
	"""
	Calculate hamming distance between 2 seqs and return as int
	Input: seqs --> list of two strings
	ASSUMPTIONS: seqs are equal lengths and dna seqs
	"""
	hamming = 0
	for i in range(0, len(seqs[1])):
		if seqs[1][i] == 'T': 
			if seqs[0][i] == 'T': pass
			else: hamming +=1
		elif seqs[1][i] == 'A': 
			if seqs[0][i] == 'A': pass
			else: hamming +=1
		elif seqs[1][i] == 'C': 
			if seqs[0][i] == 'C': pass
			else: hamming +=1
		elif seqs[1][i] == 'G': 
			if seqs[0][i] == 'G': pass
			else: hamming +=1
	return (hamming)


if __name__ == "__main__":
	seqs = fasta_to_list(argv[1])

	# Get all correct sequences
	correct_sequences = set()
	temp_seqs = seqs[:] # copy by value as I'll be removing elements
	for sequence in seqs:
		temp_seqs.remove(sequence)
		rev_comp = generate_reverse_complement_dna(sequence)
		if sequence in temp_seqs:
			correct_sequences.add(sequence)
		elif rev_comp in temp_seqs:
			correct_sequences.add(sequence)
	
	# Add reverse complement for each correct sequence to correct list
	correct_seq_revcomps = {generate_reverse_complement_dna(item) for item in correct_sequences}
	correct_sequences = correct_sequences.union(correct_seq_revcomps)

	# By inference, all incorrect sequences
	incorrect_seqs = [item for item in seqs if item not in correct_sequences]

	for seq in incorrect_seqs:
		for cseq in correct_sequences:
			dist = get_hamming_dist_dna([seq,cseq])
			if dist == 1:
				print("{}->{}".format(seq,cseq))
				continue
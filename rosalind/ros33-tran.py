#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find transition:transversion ratio as per
(http://rosalind.info/problems/tran/)
Input: Fasta file with two DNA strings of equal length
Output: Float --> ratio (transition:transversion ratio)
"""

import pdb
from sys import argv

from ian_bif_utilities import fasta_to_list


def transition_transverion_ratio (seq1, seq2):
	"""
	Input: Two strings, DNA seqs of equal length
	Output: Float --> ratio (transition:transversion ratio)
	"""
	transitions = 0
	transversions = 0
	purines = ['A', 'G']
	pyrimidines = ['C','T']

	for i in range(0,len(seq1)):
		if seq1[i] == seq2[i]:
			pass
		elif seq1[i] in purines and seq2[i] in purines:
			transitions += 1
		elif seq1[i] in pyrimidines and seq2[i] in pyrimidines:
			transitions += 1
		else:
			transversions += 1
	
	print('versions ', transversions)
	print('sitions ', transitions)
	print('Ratio ', transitions/transversions)		

if __name__ == "__main__":
	seq1, seq2 = fasta_to_list(argv[1])
	transition_transverion_ratio(seq1, seq2)
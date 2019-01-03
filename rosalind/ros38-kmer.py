#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find no. appearances of each kmer in string as per
http://rosalind.info/problems/kmer/
Input: Fasta file path, one DNA seq 
Output: Printed Ints, the number of times each kmer occurs (lexicographically ordered)
"""

from sys import argv
import pdb

from ian_bif_utilities import single_fasta_to_string

def get_kmers (k, seq):
	"""
	Get all kmers of length k from a string
	Input: INT k, STRING seq
	Output: LIST of kmers
	"""
	kmers = []
	for i in range(0, len(seq) - (k-1)):
		kmers.append(seq[i:i+4])
	return kmers


if __name__ == "__main__":
	seq = single_fasta_to_string(argv[1])
	kmers = get_kmers(4, seq)
	print(kmers)
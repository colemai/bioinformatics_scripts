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
from itertools import product 

from ian_bif_utilities import single_fasta_to_string

def get_kmers (k, alphabet):
	"""
	Get all kmers of length k from a custom alphabet e.g "ACGT"
	Input: INT k, STRING alphabet
	Output: LIST of all possible kmers in alphabetical order
	"""
	kmers = list(product(alphabet, repeat=k))
	kmers = [''.join(x) for x in kmers]
	kmers = sorted(kmers)
	return kmers

def get_kmers_v2 (k, seq):
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
	
	# First get all theoretical 4-mers, then get all 4-mers occuring in seq
	kmers = get_kmers(4, 'ACGT')
	occurence_kmers = get_kmers_v2(4, seq)
	
	# Count how many times each theoretical 4-mer exists in occuring 4-mers list
	output = []
	for kmer in kmers:
		output.append(occurence_kmers.count(kmer))

	for i in output:
		print(i, end=" ")

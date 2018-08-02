#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find no. perfect matchings RNA as per 
http://rosalind.info/problems/cat/
Input: Fasta file path, one RNA seq
Output: Int, number of perfect matchings
"""


from sys import argv
import pdb

from ian_bif_utilities import single_fasta_to_string


if __name__ == "__main__":
	seq = single_fasta_to_string(argv[1])
	print(seq)
	
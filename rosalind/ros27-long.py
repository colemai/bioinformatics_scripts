#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Return contig for multiple reads
Input: Fasta file path, DNA seqs
Output: String, superstring of all DNA seqs
"""

from sys import argv
import pdb

from ian_bif_utilities import fasta_to_list




if __name__ == "__main__":
	reads = fasta_to_list(argv[1])
	print(reads)

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


if __name__ == "__main__":
	seq_t, seq_s = fasta_to_list(argv[1])
	print(seq_t, seq_s)
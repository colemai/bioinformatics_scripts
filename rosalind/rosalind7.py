#!/usr/bin/python3
"""
Author: Ian Coleman
Purpose: Translate RNA seq into DNA seq
"""

from sys import argv

def translate_rna_to_dna (rna_seq):
	with open(rna_seq, 'r') as input_seq:
		input_seq = input_seq.readlines()[0]
		

translate_rna_to_dna(argv[1])
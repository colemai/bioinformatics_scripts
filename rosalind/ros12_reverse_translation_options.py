#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: a single protein in the form of a string in a text file
Output: The int number of reverse translation possibilities of that sequence modulo 1,000,000
"""

from sys import argv
import pdb 

def import_single_string (input_file):
	"""
	Input: File containing single string on one line
	Output: That string as a string
	"""
	with open(input_file) as file_object:
		seq = file_object.read().strip()
	return seq

def aa_to_codons (aa):
	"""
	Input: an amino acid single-char symble
	Output: the number of RNA codons that could have coded for that amino acid, int
	NOTE: Stop codon represented by *
	"""
	#TODO make input uppercase
	return {
		'E': 2, 
		'V': 4, 
		'H': 2, 
		'D': 2, 
		'G': 4, 
		'S': 6, 
		'I': 3, 
		'L': 6, 
		'C': 2, 
		'M': 1, 
		'N': 2, 
		'A': 4, 
		'Q': 2, 
		'Y': 2, 
		'P': 4, 
		'*': 3, 
		'T': 4, 
		'W': 1, 
		'K': 2, 
		'R': 6, 
		'F': 2
	}.get(aa, '')

def calculate_modulo_reverse_translations (seq):
	"""
	Input: A single string protein sequence
	Output: The int number of reverse translation possibilities of that sequence modulo 1,000,000
	TODO: try again on the more compute friendly way to do this (commented out lines + move the if)
	"""
	possible_translations = 1
	for aa in seq:
		number_codons = aa_to_codons(aa)
		occurences_aa = seq.count(aa)
		possible_translations *= number_codons
		# possible_translations *= (number_codons^occurences_aa)
		# seq = seq.replace(aa, '')

	#multiply  * 3 due for the stop codon possibilities
	possible_translations *= 3
	possible_translations = possible_translations % 1000000
	return possible_translations

if __name__ == "__main__":
	seq = import_single_string(argv[1])
	possible_translations = calculate_modulo_reverse_translations(seq)
	print(possible_translations)
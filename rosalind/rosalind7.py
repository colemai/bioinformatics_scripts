#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Translate RNA seq into protein
"""

from sys import argv

def rna_to_aa_case (rna_codon):
	"""
	Input: An RNA codon
	Output: the corresponding AA (represented by a single letter)
	Note: 'Stop' will be returned by a stop codon
	"""

	return {
		'AUG': 'R',
		'UUU': 'F',      
		'CUU': 'L',
		'AUU': 'I',      
		'GUU': 'V',
		'UUC': 'F',
		'CUC': 'L',
		'AUC': 'I',      
		'GUC': 'V',
		'UUA': 'L',      
		'CUA': 'L',
		'AUA': 'I',
		'GUA': 'V',
		'UUG': 'L',      
		'CUG': 'L',
		'AUG': 'M',
		'GUG': 'V',
		'UCU': 'S' ,     
		'CCU': 'P',
		'ACU': 'T',
		'GCU': 'A',
		'UCC': 'S' ,     
		'CCC': 'P',
		'ACC': 'T',
		'GCC': 'A',
		'UCA': 'S' ,     
		'CCA': 'P',
		'ACA': 'T',
		'GCA': 'A',
		'UCG': 'S' ,     
		'CCG': 'P',
		'ACG': 'T',
		'GCG': 'A',
		'UAU': 'Y' ,     
		'CAU': 'H',
		'AAU': 'N',
		'GAU': 'D',
		'UAC': 'Y' ,     
		'CAC': 'H',
		'AAC': 'N',
		'GAC': 'D',
		'UAA': 'Stop',   
		'CAA': 'Q',
		'AAA': 'K',
		'GAA': 'E',
		'UAG': 'Stop',  
		'CAG': 'Q',
		'AAG': 'K',
		'GAG': 'E',
		'UGU': 'C',      
		'CGU': 'R',
		'AGU': 'S',
		'GGU': 'G',
		'UGC': 'C',      
		'CGC': 'R',
		'AGC': 'S',
		'GGC': 'G',
		'UGA': 'Stop',   
		'CGA': 'R',
		'AGA': 'R',
		'GGA': 'G',
		'UGG': 'W',      
		'CGG': 'R',
		'AGG': 'R',
		'GGG': 'G'
	}.get(rna_codon, 0)

def rna_to_codons(rna_string):
	"""
	Input: RNA string (or any string)
	Output: List of codons (string split into sets of three chars)
	Note: If string is not divisible by three then the last codon will be one or two chars
	"""
	codon_list = []
	for i in range(0, len(rna_string), 3):
		codon_list.append(rna_string[i:i+3])
	return (codon_list)

def translate_rna(rna_string):
	"""
	Runs two above commands to:
	Input: RNA string
	Output: Translated Protein in one-char AAs
	"""
	protein = ''
	codons = rna_to_codons(rna_string)
	for codon in codons:
		if rna_to_aa_case(codon) == 'Stop':
			break
		else:
			protein += rna_to_aa_case(codon)
	print(protein)

if __name__ == "__main__":
	with open(argv[1], 'r') as file_object:
		file_list = file_object.readlines()
		translate_rna(file_list[0])
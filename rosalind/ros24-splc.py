#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A fasta file where the first seq is a DNA seq and the rest are introns within it
Output: The translated output of that DNA seq minus those introns (String)
Example call: python3 ros24-splc.py sequences.txt
"""

from sys import argv
import pdb

from ian_bif_utilities import fasta_to_list
from ian_bif_utilities import dna_to_rna
from ian_bif_utilities import rna_to_codons
from ian_bif_utilities import rna_to_aa

def splice_introns (dna, introns):
	"""
	Input: dna (string), introns (list of strings --> must each be contained within dna) 
	Output: single string --> peptide sequence, dna without introns translated
	"""
	# print(dna)
	for intron in introns:
		dna = dna.replace(intron, '')
	# print(dna)
	return(dna)

def codons_to_protein (codons):
	"""
	REQUIRES: rna_to_aa function
	Input: List of strings (codons)
	Output: String (protein seq)
	"""
	protein = ''
	for codon in codons:
		protein += rna_to_aa(codon)
	return protein

if __name__ == "__main__":
	# Import data
	seqs = fasta_to_list(argv[1])
	dna = seqs[0]
	introns = seqs[1:]

	# Convert step-by-step from DNA to Protein
	coding_dna = splice_introns(dna, introns)
	mrna = dna_to_rna(coding_dna)
	codons = rna_to_codons(mrna)
	protein = codons_to_protein(codons)
	
	print(protein[:-1]) # return everything except the stop codon

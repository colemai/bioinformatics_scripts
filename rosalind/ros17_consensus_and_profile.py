#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A Fasta file with multiple DNA seqs of equal length
Output: Consensus string followed by profile matrix

Challenge description: http://rosalind.info/problems/cons/

"""

from sys import argv
import pdb

def intake_data(file_path):
	"""
	Input: Path to fast file with multiple DNA seqs of equal length
	Output: Array of seqs
	"""
	with open(file_path, 'r') as file_object:
		lines_list = file_object.readlines()
		seq_list = []
		for line in lines_list:
			if not line.startswith('>'):
				seq_list.append(line.strip())
		return seq_list

def make_profile_matrix(seq_list):
	"""
	Input: List of DNA sequences of equal length
	Output: Profile Matrix (4 x length of seqs)
	"""



if __name__ == "__main__":
	seq_list = intake_data(argv[1])
	
	#Test that seqs meet criteria
	assert len(seq_list) > 1
	for seq in seq_list:
		assert len(seq) == len(seq_list[-1]), \
		"The sequences are not of equal length..."
		
	profile_matrix = make_profile_matrix(seq_list)
	
#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A Fasta file with multiple DNA seqs of equal length
Output: Consensus string followed by profile matrix
Note: Expects uppercase seqs

Challenge description: http://rosalind.info/problems/cons/

"""

from sys import argv
import pdb
import numpy as np

def intake_data(file_path):
	"""
	Input: Path to fasta file with multiple DNA seqs of equal length
	Output: Numpy-array of seqs
	"""
	with open(file_path, 'r') as file_object:
		lines_list = file_object.readlines()
		seq_list = []
		for line in lines_list:
			if not line.startswith('>'):
				seq_list.append(line.strip())
		return seq_list

# def make_profile_matrix(seq_list):
# 	"""
# 	Input: Numpy-array of DNA sequences of equal length
# 	Output: Profile Matrix (4 x length of seqs, as np array)
# 	"""
# 	counts = []
# 	for i in ['A','C','G','T']: counts.append(np.char.count(seq_list, i))
# 	print(seq_list)
# 	print(np.vstack(counts))

def make_profile_matrix(seq_list):
	"""
	Input: Numpy-array of DNA sequences of equal length
	Output: Profile Matrix (4 x length of seqs, as np array)
	"""

	labels = ['A','C', 'G','T']

	# Get matrix of individual bases of each seq
	split_chars = []
	for seq in seq_list: 
		split_chars.append(list(seq))
	base_matrix = np.vstack(split_chars) 

	# Create string of each column as though it were a seq
	base_matrix_t = np.transpose(base_matrix)
	columns = []
	for i in range(0,base_matrix_t.shape[0]):
		string = ""
		for base in base_matrix_t[i]:
			string += base
		columns.append(string)
	print(columns)

	# Count and Return profile matrix 
	counts = []
	for i in ['A','C','G','T']: counts.append(np.char.count(columns, i))
	return(np.vstack(counts))
		



def make_consensus_seq(profile_matrix):
	"""
	Input: Profile Matrix (4 x length of seqs, as np array)
	Output: Consensus Sequence as string
	"""
	labels = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
	consensus = ""
	highest_values = np.argmax(profile_matrix, axis=0)
	for i in highest_values: 
		consensus += labels[i]
	return consensus





if __name__ == "__main__":
	seq_list = intake_data(argv[1])

	#Test that seqs meet criteria
	assert len(seq_list) > 1
	for seq in seq_list:
		assert len(seq) == len(seq_list[-1]), \
		"The sequences are not of equal length..."
		
	profile_matrix = make_profile_matrix(seq_list)
	consensus = make_consensus_seq(profile_matrix)
	# print(consensus)
	
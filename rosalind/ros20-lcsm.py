#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A fasta file with multiple DNA seqs
Output: The longest common subsequence
Note: Assumes seqs are unique

Challenge description: http://rosalind.info/problems/lcsm/

"""

from sys import argv
import pdb

def intake_data(file_path):
	"""
	Input: Path to fasta file with multiple DNA seqs of equal length
	Output: List of seqs
	"""
	with open(file_path, 'r') as file_object:
		lines_list = file_object.readlines()
		seq_list = []
		current_seq = ''
		for line in lines_list:
			if line.startswith('>'):
				seq_list.append('')
				current_seq = ''
			else:
				seq_list[-1] += line.strip()
	return seq_list

def longest_common_substr(seqs):
	"""
	Input: List of strings
	Output: Longest common substring of those strings
	"""
	lcs = ''

	#iterate through each sequence (actually I end up returning after first seq)
	for seq in seqs:
		#copy seqs (by value, not ref) to safely remove the current seq --> making a comparison list
		copy_seqs = seqs[:]
		copy_seqs.remove(seq)

		#Iterate through each index of sequence
		for i in range(0, len(seq)):
			
			# For this index create a substring at least as long as the current lcs
			next_char = i + len(lcs) 
			substr = seq[i : next_char + 1]

			#if substring is common to all seqs then repeatedly expand it with next character in line
			is_common = all(substr in item for item in (copy_seqs))
			while is_common and len(seq) > next_char +1:
				next_char += 1
				substr += seq[next_char]
				is_common = all(substr in item for item in (copy_seqs))

			# When substring can no longer be expanded, store it if it's the longest common substring so far
			if is_common and len(substr) > len(lcs): 
				lcs = substr
			elif len(substr) -1 > len(lcs) and not is_common:
				lcs = (substr[:-1])				
		return lcs


if __name__ == "__main__":
	seqs = intake_data(argv[1])
	lcs = longest_common_substr(seqs)
	print(lcs)
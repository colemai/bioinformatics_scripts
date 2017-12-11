#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Fasta File
Output: Longest substring common to all sequences
Note: If there is a tie, only one substring will be returned regardless
"""

from sys import argv
import pdb

def parse_fasta (input_filename):
	"""
	Input: Fasta File
	Output: Dictionary of {label: sequence} both strings
	"""
	with open(input_filename, 'r') as file_object:
		file_list = file_object.readlines()
		fasta_dict = {}
		for i in range(0, len(file_list)):
			if file_list[i].startswith('>'):
				label_index = file_list[i].strip()[1:]
				fasta_dict[label_index] = ''
			else: 
				fasta_dict[label_index] += file_list[i].strip()
		return fasta_dict

def removekey(d, key):
	r = dict(d)
	del r[key]
	return r

def longest_common_substring (fasta):
	"""
	Input: Fasta Dict {name: seq, name: seq}
	Output: Longest common substring (of sequences)
	"""
	pdb.set_trace()
	common_substrings = []
	for label,seq in fasta.items():
		comparison = seq
		#create dict without current sequence
		comparators = removekey(fasta,label)
		#iterate through the modified dict
		#iterate through the chars in comparison-seq, find all occurences in the other seqs, add the next char to the comparison seq until
		#there is no match then add the last match(es) to the output
		#Repeat for all seqs (make each comparison seq in turn)
		for label2,seq2 in comparators.items():
			for i in range(0, min([len(comparison), len(seq2)])):
				print (comparison, seq2, seq2[i])

def find_longest_subs(comparison, comparators):
	'''
	Input: A string, a list of strings
	Output: The longest substring occurring between the comparison string and each string in the list of strings
	'''
	#iterate through each char (search string) in comparison
	for index in range(1, len(comparison) + 1):
		search_char = comparison[0:index]
		findings = []
		#find all occurrences of this char in comparators, overwrite list with findings - actual string
		if any(search_char in s for s in comparators):
			findings = [search_char]
			print(findings)
		#add the next char to the search string
		#search again
		#when nothing matches the search string, return findings


if __name__ == "__main__":
	#Step1: import fasta and establish list of sequences
	fasta_dict = parse_fasta(argv[1])
	seqs_list = []
	for key, value in fasta_dict.items():
		seqs_list.append(value)
	
	#Step2: Iterate through sequences and find longest
	for seq in seqs_list:
		find_longest_subs(seq, seqs_list.remove(seq)) #the comparatores list would be better if it removed all occurences of seq which this won't

	print (seqs_list)
	# longest_common_substring = longest_common_substring(fasta_dict)
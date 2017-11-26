#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Create overlap graph (O3, where overlap is three) for sequences in a given fasta file
Input: Fasta file of sequences of any string
"""

from sys import argv
import functools
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

def adjacency_list (fasta_dict):
	"""
	Input: Fasta dictionary of {label: sequence} both strings
	Output: Adjacency list of O3 overlap graph for these sequences
	"""
	adj_list = []
	k = ''
	label = ''
	for key,value in fasta_dict.items():
		other_sequences = removekey(fasta_dict, key)
		for key2,value2 in other_sequences.items():
			if value[-3:] == value2[:3]:
				adj_list.append((key, key2))
	return adj_list

if __name__ == "__main__":
	fasta = parse_fasta(argv[1])
	adj_list = adjacency_list(fasta)
	for key, value in adj_list:
		print(key, value)
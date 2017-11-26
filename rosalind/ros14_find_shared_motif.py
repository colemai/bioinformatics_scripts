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

if __name__ == "__main__":
	fasta_dict = parse_fasta(argv[1])
	print (fasta_dict)
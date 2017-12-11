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
    Input: List of strings
    Output: Longest common substring
    """
    common_substrings = []
    for label,seq in fasta.items():
        comparison = seq
        comparators = removekey(fasta,label)
        for label2,seq2 in comparators.items():
            for i in range(0, min([len(comparison), len(seq2)])):
                print (comparison, seq2, seq2[i])
            


if __name__ == "__main__":
	fasta_dict = parse_fasta(argv[1])
	longest_common_substring = longest_common_substring(fasta_dict)
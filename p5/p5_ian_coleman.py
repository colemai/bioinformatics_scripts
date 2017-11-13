#!/usr/bin/env python3
"""
Author: Ian Coleman
Student Number: 910616-160-090
Purpose: Carry out a pairwise alignment for each seq in an input fasta relative to a given reference seq
Input: 1. Reference seq in fasta format (single seq) 2. Fasta file with all seqs to compare with ref seq
Output: Tab delimited 
"""

from sys import argv
import subprocess

#to do: check Sandra's docstrings
# a bunch of asserting

def parse_fasta (input_filename):
    #Converts fasta file into a dictionary. Input of fasta file.
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        master_seq_list = []
        fasta_dict = {}
        #iterate through each line, add label as key and sequence as value
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                label_index = file_list[i].strip()
                fasta_dict['Label'] = label_index
                fasta_dict['Sequence'] = ''
            else: 
                fasta_dict['Sequence'] += file_list[i].strip()
            master_seq_list.append(fasta_dict)
        return master_seq_list

def add_lengths_to_seqs (seqs_list):
	for seq in seqs_list:
		seq['Length'] = len(seq['Sequence'])
	return seqs_list

def prep_seqs(fasta_input):
	seqs = parse_fasta(fasta_input)
	seqs_with_length = add_lengths_to_seqs(seqs)
	return seqs_with_length

def call_needle(ref_seq, other_seq, gap_open = 8, gap_extend = 0.5, out_file = 'out.needle'):
    cmd = 'needle {} {} -gapopen {} -gapextend {} -outfile {}'\
    .format(ref_seq, other_seq, gap_open, gap_extend, out_file)
    err = subprocess.check_output(cmd, shell=True)
    result = subprocess.check_call(cmd, shell=True)

def pairwise_align(ref_seq, seqs):
	"""
	Input: ref seq which is a single seq dict in a list, seqs which are multiple
	Function: Pairwise aligns each of seqs with ref seq using needle programme
	Output: 
	"""
	for sequence in seqs:
		reference = ref_seq[1]['Sequence']
		current_sequence = sequence['Sequence']
		
		call_needle(reference, current_sequence)

if __name__ == "__main__":
    #run the methods
	reference_sequence = prep_seqs(argv[1])
	non_reference_sequences = prep_seqs(argv[2])
	
	call_needle(argv[1], argv[2])


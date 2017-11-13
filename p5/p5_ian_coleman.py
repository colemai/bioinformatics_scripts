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
# output identity as float of two decimal places

def parse_fasta (input_filename):
    #Converts fasta file into a dictionary. Input of fasta file.
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        master_seq_list = []
        fasta_dict = {}
        #iterate through each line, add label as key and sequence as value
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                if fasta_dict: master_seq_list.append(fasta_dict)
                fasta_dict = {}
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

def hamming_distance (seq1, seq2):
	"""
	Input: Two Sequences of equal length
	Output: Hamming distance between those two sequences
	"""
	hamming = 0

	for i in range(0, len(seq1)):
		if seq1[i] != seq2[i]:
			hamming +=1
		else:
			continue
	return hamming

def identity_with_ref (ref, seq):
	"""
	Input: two sequences
	Output: identity of the sequences (no identical position/alignment length * 100)
	Assumes alignment is length of the shorter seq
	"""

	lengths = [len(ref), len(seq)]
	alignment_length = min(lengths)
	identical_positions = hamming_distance(ref, seq)
	identity = (identical_positions/alignment_length) * 100
	print (identity)


# def pairwise_align(ref_seq, seqs):
# 	"""
# 	Input: ref seq which is a single seq dict in a list, seqs which are multiple
# 	Function: Pairwise aligns each of seqs with ref seq using needle programme
# 	Output: 
# 	"""
# 	for sequence in seqs:
# 		reference = ref_seq[1]['Sequence']
# 		current_sequence = sequence['Sequence']
		
# 		call_needle(reference, current_sequence)

if __name__ == "__main__":
    #run the methods
	reference_sequence = prep_seqs(argv[1])
	non_reference_sequences = prep_seqs(argv[2])
	# print (non_reference_sequences)
	
	# call_needle(argv[1], argv[2])
	# hamming_distance(reference_sequence[0]['Sequence'], non_reference_sequences[2]['Sequence'])
	identity_with_ref(reference_sequence[0]['Sequence'], non_reference_sequences[1]['Sequence'])




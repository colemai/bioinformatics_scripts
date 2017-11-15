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
import os.path
import sys

def parse_fasta (input_filename):
    #Converts fasta file into a list of dictionaries. Input of fasta file.
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
	lengths = [len(seq1), len(seq2)]

	for i in range(0, min(lengths)):
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

def parse_needle_output(needle_file_name):
	"""
	Input: The output file of needle (EMBOSS command line tool for pairwise alignment)
	Output: List of lists, the sub lists containing a string of each line of a given alignment
	"""
	if os.path.isfile(needle_file_name):
		output_file_path = (os.path.join(sys.path[0], needle_file_name))
		with open(output_file_path, 'r') as needle_file:
			needle_text = needle_file.readlines()
			master_needle = []
			single_alignment = []
			for line in needle_text:
				if "Aligned_sequences" in line:
					master_needle.append(single_alignment)
					single_alignment = []
					single_alignment.append(line.strip())
				else:
					single_alignment.append(line.strip())
			master_needle.append(single_alignment)
			del master_needle[0]
			return(master_needle[0])

def give_tab_delimited_summary(seqs, ref_seq):
	"""
	Input: 
	Output: Returns tab delimited table summarising each alignment (seq1, length, seq2, len, hamm, ident)
	"""

	ref_seq_name = ref_seq[0]['Label'] + '\t'
	ref_seq_length = str(ref_seq[0]['Length']) + '\t'

	with open('alignment_summary.txt', 'w') as file_object:
		for seq in seqs:
			seq_name = seq['Label'] + '\t'
			seq_length = str(seq['Length']) + '\t'
			hamm = str(hamming_distance(ref_seq[0]['Sequence'], seq['Sequence'])) + '\t'
			ident = str(identity_with_ref(ref_seq[0]['Sequence'], seq['Sequence'])) + '\n'
			file_object.write(ref_seq_name)
			file_object.write(ref_seq_length)
			file_object.write(seq_name)
			file_object.write(seq_length)
			file_object.write(hamm)
			file_object.write(ident)

if __name__ == "__main__":
    #run the methods
	reference_sequence = prep_seqs(argv[1])
	non_reference_sequences = prep_seqs(argv[2])
	
	parse_needle_output('out.needle')
	give_tab_delimited_summary(non_reference_sequences, reference_sequence)




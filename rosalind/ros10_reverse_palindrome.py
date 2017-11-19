#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find the position and length of every reverse palindrome in a given DNA seq
of length between 4 and 12
"""

from sys import argv

#Step 1 import single fasta file (utils)
def single_fasta_to_string (input_file):
	"""
	Input: Fasta file with single fasta entry
	Output: Sequence string
	"""
	with open(input_file) as fasta_file:
		lines = fasta_file.readlines()
		#get the stripped version of every line after the first line joined up
		forward_sequence = ''.join(list(map(str.strip, lines[1:])))
	return(forward_sequence)

#Step 2 convert seq into its reverse complement (utils)
def generate_reverse_complement_dna (forward_sequence):
	"""
	Input: Dna sequence as string
	Output: The reverse complement of that sequence as a string
	"""
	reverse_complement = ''
	reverse_forward_sequence = forward_sequence[::-1]
	dna_dict = {
		'A':'T',
		'T':'A',
		'G':'C',
		'C':'G'
	}
	for nt in reverse_forward_sequence:
		reverse_complement += dna_dict.get(nt)
	return (reverse_complement)

#Step 3 find all locations of similarities
def find_reverse_palindromes (seq, reverse_complement):
	"""
	Input: a DNA sequence and its reverse palindrome as strings
	Output: list of [position, length] of palindromes with len >= 4
	"""
	final_list_palindromes = []
	#iterate through sequence (until last three chars as only want palindroms with len >= 4)
	for index in range(0, len(seq) - 3):
		#for each index go check the strings of lengths 4 to 12
		for i in range(4, 13):
			#if the string in question == its own reverse complement then store it
			if (index + i <= len(seq)):
				if seq[index: index + i] == generate_reverse_complement_dna(seq[index: index + i]):
					final_list_palindromes.append((index + 1, i))
	return final_list_palindromes

#Step 4 Run methods
if __name__ == "__main__":
	seq = single_fasta_to_string(argv[1])
	reverse_complement = generate_reverse_complement_dna (seq)
	reverse_palindromes = find_reverse_palindromes(seq, reverse_complement)
	for e in reverse_palindromes: 
		print (e[0], e[1])


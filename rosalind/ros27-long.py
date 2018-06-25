#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Return contig for multiple reads
Input: Fasta file path, DNA seqs (must all overlap)
Output: String, superstring of all DNA seqs
"""

from sys import argv
import pdb

from ian_bif_utilities import fasta_to_list

def make_contig (reads):
	"""
	Input: list of strings, DNA sequences (must all overlap)
	Output: string, contig of all of those strings
	"""

	# contig = reads[0]
	# remaining_reads = copy_reads
	# remaining_reads - contig
	# for read in reads:
	# min_overlap = half_length_read
	# if read is contained in contig
	#	remaining_reads - read
	#	skip
	# if first min_overlap of contig is the same as last min_overlap read
	#	attach read to start of contig appropriately
	#	remaining_reads - read
	# if last min_overlap of contig is the same as first min_overlap read
	#	attach read to end of contig appropriately
	#	remaining_reads - read
	# 
	# check if each read is only present once in the contig

	# This gives a contig but not necessarily the shortest one

	# contig = reads[1] #change this to random
	# remaining_reads = reads[:] # remove the contig read
	# # while len(remaining_reads) != 0:
	# for i in range(0, len(remaining_reads)):
	# 	pdb.set_trace()
	# 	read = remaining_reads[i]
	# 	min_overlap = int(len(read)/2)
	# 	if read in contig:
	# 		remaining_reads[i] = contig[0]
	# 		# remaining_reads.remove(read)
	# 	elif contig[:min_overlap] == read[-min_overlap:]:
	# 		overlap = contig[:min_overlap]
	# 		pdb.set_trace()
	# 		# for letter in read[-min_overlap::-1]:
	# 			# if   	 	
	# # must be a way to break out of while loop if infinite

	# if half_of_read in contig
	# if half_of_read in first half of contig:
	# if contig[:end_of half_of_read]


	# SIMPLEST
	# overlap = ''
	# for letter in contig:
	# while overlap + (letter + 1) in contig
	# overlap += letter + 1
	# letter_ind + 1


	# Iterates through each of the reads, finds its longest overlap with first read and adds it to list
	contig = reads[0]
	overlaps = []
	for i in range(0, len(reads) - 1):
		# pdb.set_trace()
		read = reads[1:][i]
		overlap = ''
		temp_contig = ''
		
		for j in range(0, len(read)):
			# overlap = ''
			while j < len(read) and (overlap + read[j]) in contig:
				overlap += read[j]
				j += 1	
				# pdb.set_trace()
			if len(overlap) > len(temp_contig):
				temp_contig = overlap
		# pdb.set_trace()
		overlaps.append(temp_contig)
	return overlaps


if __name__ == "__main__":
	reads = fasta_to_list(argv[1])
	result = make_contig(reads)
	print(result)

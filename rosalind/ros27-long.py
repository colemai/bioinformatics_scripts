#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Return contig for multiple reads
Input: Fasta file path, DNA seqs (must all overlap)
Output: String, superstring of all DNA seqs, Boolean (False if no read matches)
"""

from sys import argv
import pdb
import random

from ian_bif_utilities import fasta_to_list


def add_first_big_overlap (reads, contig):
	"""
	Input: list (reads), string (contig)
	Output: list (reads - added read), string(improved contig), boolean (False 
	if no reads overlap more than half their length)
	"""

	#Set initial length
	initial_length = len(contig)

	# Iterate through the reads
	for read in reads:
		print('New read loop')
		print(len(contig))

		# Find this read's biggest overlap
		best_overlap = ''
		for j in range(0, len(read)):
			overlap = ''
			while j < len(read) and (overlap + read[j]) in contig:
				overlap += read[j]
				j += 1	
			if len(overlap) > len(best_overlap):
				best_overlap = overlap
			if (len(read) - j) < len(best_overlap):
				# pdb.set_trace()
				break
			if (len(read) - j) < int(len(read)/2):
				break
			# if (remaining_chars < len(best_overlap) or half_read_len) and overlap

		# If the overlap is greater than half the read's length, add to contig and return
		if len(best_overlap) < int(len(read)/2) + 1:
			continue

		# if the overlap is at the end of the read, chop and add to start contig
		if best_overlap == contig[-len(best_overlap):]:
			contig += read[len(best_overlap):]
			reads.remove(read)
			return reads, contig, False
		# if the overlap as at the beginning of the read, chop and add to end contig
		elif best_overlap == contig[:len(best_overlap)]:
			contig = read[:(len(read)-len(best_overlap))] + contig
			reads.remove(read)
			return reads, contig, False

	return reads, contig, True

def random_contig (reads):
	"""
	REQUIRES add_first_big_overlap
	Input: list (reads)
	Output: string (contig with degree of randomisation)
	"""
	contig = random.choice(reads)
	reads_draft = reads[:]
	reads_draft.remove(contig)

	stuck = False 
	while len(reads_draft) != 0:
		reads_draft, contig, stuck = add_first_big_overlap(reads_draft,contig)
		if stuck: 
			print('STUCK! Shuffling and restarting')
			contig = random.choice(reads)
			reads_draft = reads[:]
			reads_draft.remove(contig)
	return reads, contig, stuck


if __name__ == "__main__":
	# Get Reads
	reads = fasta_to_list(argv[1])

	# Get Superstring
	reads, contig, stuck = random_contig (reads)

	# Print Superstring 
	print(contig, stuck)



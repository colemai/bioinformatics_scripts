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


def overlap_append (reads, contig):
	for i in range(0, len(reads)):
		print('new_loop')
		read = reads[i] 
		overlap = ''
		best_overlap = ''
		
		if read in contig:
			print('Read is contained')
			reads.remove(read)
			return reads,contig
			# continue

		print('Working on read ', read)
		for j in range(0, len(read)):
			while j < len(read) and (overlap + read[j]) in contig:
				overlap += read[j]
				j += 1	
				# print('While loop with j ', j)
			if len(overlap) > len(best_overlap):
				best_overlap = overlap

		print('Overall best overlap for read: ', best_overlap)

		if len(best_overlap) < int(len(read)/2):
			print('continuing')
			continue

		# print(read, best_overlap)
		# if the overlap as at the end of the read, chop and add to start contig
		if best_overlap == contig[-len(best_overlap):]:
			print('overlaps at end')
			contig += read[len(best_overlap):]
			reads.remove(read)
			return reads, contig
		elif best_overlap == contig[:len(best_overlap)]:
			print('Overlaps at beginning')
			pdb.set_trace()
			contig = read[:len(best_overlap)] + contig
			reads.remove(read)
			return reads, contig
		else:
			print('read ', read, ' did not match, continuing')

	#return reads, contig

if __name__ == "__main__":
	reads = fasta_to_list(argv[1])
	# contig = reads[0]
	# reads.remove(contig)

	while len(reads) != 0:
		for i in range(0,len(reads)):
			contig = reads[i]
			print('New Contig: ', contig)
			remaining_reads = reads[:]
			remaining_reads.remove(contig)
			for j in range(0,len(reads)):
				print('Current reads ', remaining_reads, ' and contig ', contig)
				if len(remaining_reads) > 0:
					reads, contig = overlap_append(remaining_reads,contig)
				else:
					print('-------')
					print(contig)
					print('-------')

		print('while loop with contig ', contig)

	print('Finally', reads, contig)

#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Return contig for multiple reads
Input: Fasta file path, DNA seqs (must all overlap)
Output: String, superstring of all DNA seqs
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
	#TODO stop j iterations when rest of read is less than length biggest overlap AND
	#current overlap is less than the length of the biggest overlap
	# Or biggest overlap is less than half_len AND j is past halfway AND current_overlap < length 1

	#Set initial length
	initial_length = len(contig)

	# Iterate through the reads
	for read in reads:

		# Find this read's biggest overlap
		best_overlap = ''
		for j in range(0, len(read)):
				overlap = ''
				while j < len(read) and (overlap + read[j]) in contig:
					overlap += read[j]
					j += 1	
				if len(overlap) > len(best_overlap):
					best_overlap = overlap

		# If the overlap is greater than half the read's length, add to contig and return
		if len(best_overlap) < int(len(read)/2):
				# print('continuing')
				continue

		# if the overlap is at the end of the read, chop and add to start contig
		if best_overlap == contig[-len(best_overlap):]:
			contig += read[len(best_overlap):]
			reads.remove(read)
			return reads, contig, False
		# if the overlap as at the beginning of the read, chop and add to end contig
		elif best_overlap == contig[:len(best_overlap)]:
			print('Overlaps at beginning')
			# pdb.set_trace()
			contig = read[:len(best_overlap)-1] + contig
			reads.remove(read)
			return reads, contig, False

	return reads, contig, True

def add_biggest_overlap (reads, contig):
	"""
	Input: list (reads), string (contig)
	Output: list (reads - added read), string(improved contig), boolean (False 
	if no reads overlap more than half their length)
	"""
	#TODO stop j iterations when rest of read is less than length biggest overlap AND
	#current overlap is less than the length of the biggest overlap
	# Or biggest overlap is less than half_len AND j is past halfway AND current_overlap < length 1

	#Set initial length
	initial_length = len(contig)

	# Iterate through the reads
	overlaps = []
	for read in reads:

		# Find this read's biggest overlap
		best_overlap = ''
		for j in range(0, len(read)):
				overlap = ''
				while j < len(read) and (overlap + read[j]) in contig:
					overlap += read[j]
					j += 1	
				if len(overlap) > len(best_overlap):
					best_overlap = overlap

		# Add it to the list of reads' best overlaps
		overlaps.append(best_overlap)

	overlap_index, longest_overlap = max(enumerate(overlaps), key=lambda x: len(x[1]))
	overlapping_read = reads[overlap_index]

	# If the overlap is greater than half the read's length, add to contig and return
	if len(longest_overlap) < int(len(overlapping_read)/2):
		return reads, contig, True
	elif longest_overlap == contig[-len(longest_overlap):]:
		contig += overlapping_read[len(longest_overlap):]
		reads.remove(overlapping_read)
		return reads, contig, False
		# if the overlap as at the beginning of the read, chop and add to end contig
	elif longest_overlap == contig[:len(longest_overlap)]:
		print('Overlaps at beginning')
		# pdb.set_trace()
		contig = overlapping_read[:len(longest_overlap)-1] + contig
		reads.remove(overlapping_read)
		return reads, contig, False

	print('FAILFAILFAIL should have returned by now')


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
			# contig = reads[0]
			contig = random.choice(reads)
			reads_draft = reads[:]
			reads_draft.remove(contig)
			# random.shuffle(reads_draft) 
	return reads, contig, stuck

if __name__ == "__main__":
	# Get Reads
	reads = fasta_to_list(argv[1])

	reads, contig, stuck = random_contig (reads)
	print(contig, stuck)
	exit()
	# Make first addition to Contig
	contig = reads[0]
	reads = reads[1:]
	reads,contig,success = add_first_big_overlap(reads, contig)
	print(contig)
	





def overlap_append (reads, contig):
	for x in range(0,10):
		for i in range(0, len(reads)):
			# print('new_loop')
			read = reads[i] 
			overlap = ''
			best_overlap = ''
			
			# print('Working on read ', read)

			if read in contig:
				# print('Read is contained')
				reads.remove(read)
				return reads,contig
				# continue

			#Find the best overlap for this word with the contig
			for j in range(0, len(read)):
				while j < len(read) and (overlap + read[j]) in contig:
					overlap += read[j]
					j += 1	
					# print('While loop with j ', j)
				if len(overlap) > len(best_overlap):
					best_overlap = overlap

			# print('Overall best overlap for read: ', best_overlap)

			# If the best overlap is at least half the length of the read, add it
			if len(best_overlap) < int(len(read)/2):
				# print('continuing')
				continue

			# print(read, best_overlap)
			# if the overlap as at the end of the read, chop and add to start contig
			if best_overlap == contig[-len(best_overlap):]:
				# print('overlaps at end')
				contig += read[len(best_overlap):]
				reads.remove(read)
				return reads, contig
			elif best_overlap == contig[:len(best_overlap)]:
				# print('Overlaps at beginning')
				pdb.set_trace()
				contig = read[:len(best_overlap)] + contig
				reads.remove(read)
				return reads, contig
			# else:
				# print('read ', read, ' did not match, continuing')

	return reads, contig

if __name__ == "__main__":
	readsers = fasta_to_list(argv[1])
	# contig = reads[0]
	# reads.remove(contig)
	remaining_reads = [1] #placeholder
	while len(remaining_reads) != 0:
		# for i in range(0,len(readsers)):
		contig = random.choice(readsers)
		# print('New Contig: ', contig)
		remaining_reads = readsers[:]
		remaining_reads.remove(contig)
		for j in range(0,len(remaining_reads)):
			# print('Current reads ', remaining_reads, ' and contig ', contig)
			# if len(remaining_reads) > 0:
			remaining_reads, contig = overlap_append(remaining_reads,contig)
			print('Current contig: ', contig)
			# else:
			# print('-------')
			# print(contig)
			# print('-------')

	# print('while loop with contig ', contig)

	print('Finally', readsers, contig)

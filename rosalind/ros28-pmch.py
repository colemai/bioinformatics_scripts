#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find total possible number of perfect basepair edge matchings as per
http://rosalind.info/problems/pmch/
Input: Fasta file path, single RNA seq (same no. A's as U's and G's as C's)
Output: Integer, Number of perfect matchings basepair edges of that seq
"""

from sys import argv
import pdb
import numpy as np
import itertools

from ian_bif_utilities import single_fasta_to_string

def find_base_edges (rna_seq):
	"""
	Input: String --> rna seq
	Output: List of tuples --> each tuple is a basepair edge, indices of bases
	"""
	print('RNA seq: ', rna_seq)
	basepair_edges = []

	for i in range(0, len(rna_seq)):

		if rna_seq[i] == 'A':
			for j in range(i+1, len(rna_seq)):
				if rna_seq[j] == 'U':
					basepair_edges.append((i, j))
		if rna_seq[i] == 'G':
			for j in range(i+1, len(rna_seq)):
				if rna_seq[j] == 'C':
					basepair_edges.append((i, j))
		if rna_seq[i] == 'C':
			for j in range(i+1, len(rna_seq)):
				if rna_seq[j] == 'G':
					basepair_edges.append((i, j))
		if rna_seq[i] == 'U':
			for j in range(i+1, len(rna_seq)):
				if rna_seq[j] == 'A':
					basepair_edges.append((i, j))
	return(basepair_edges)




# if __name__ == "__main__":
# 	rna_seq = single_fasta_to_string(argv[1])
# 	edges = find_base_edges(rna_seq)
# 	print(edges)
# 	# pdb.set_trace()
# 	# print( len(list(itertools.combinations(edges, 5))) )

# 	possible_combos = list(itertools.combinations(edges, 5))
# 	possible_combos = [list(tup) for tup in possible_combos]
# 	# print(possible_combos)
# 	# possible_combos = [[(0, 3), (0, 6), (2, 5), (4, 9), (6, 8)], [(1, 3), (7, 0), (2, 5), (4, 9), (6, 8)], [(1, 3), (2, 4), (6, 5), (7, 9), (0, 8)],]
# 	# pdb.set_trace()
# 	matchings = []
# 	tupsers =[]
# 	for combo in possible_combos:
# 		# pdb.set_trace()
# 		tmp_nums = []
# 		for tup in combo:
# 			tmp_nums.append(tup[0])
# 			tmp_nums.append(tup[1])
# 		if len(tmp_nums) > len(set(tmp_nums)):
# 			# pdb.set_trace()
# 			continue
# 		else:
# 			# pdb.set_trace()
# 			matchings.append(combo)
# 			tupsers.append(tmp_nums)

# 	# 	print('Any duplicates: ', )
# 	# 	pdb.set_trace()
# 	# 	combo.sort()
# 	# 	if len(combo) != len(set(combo)):
# 	# 		matchings.append(combo)
# 	print(len(matchings))
# 	print(matchings)
# 	# pdb.set_trace()
# 	exit()

def find_base_edges (rna_seq):
	"""
	Input: String --> rna seq
	Output: List of tuples --> each tuple is a basepair edge, indices of bases
	"""
	print('RNA seq: ', rna_seq)
	basepair_edges = []

	for i in range(0, len(rna_seq)):

		if rna_seq[i] == 'A':
			for j in range(i+2, len(rna_seq)):
				if rna_seq[j] == 'U':
					basepair_edges.append((i, j))
		if rna_seq[i] == 'G':
			for j in range(i+2, len(rna_seq)):
				if rna_seq[j] == 'C':
					basepair_edges.append((i, j))
		if rna_seq[i] == 'C':
			for j in range(i+2, len(rna_seq)):
				if rna_seq[j] == 'G':
					basepair_edges.append((i, j))
		if rna_seq[i] == 'U':
			for j in range(i+2, len(rna_seq)):
				if rna_seq[j] == 'A':
					basepair_edges.append((i, j))
	return(basepair_edges)


def count_perfect_matchings (basepair_edges, rna_seq):
	"""
	Input: List of tuples (all possible basepair bonds), String (rna seq)
	Output: Integer (no. combinations where each base used exactly once)
	"""
	probability_of_availability = np.ones(len(basepair_edges)) # make this numpy ones vector
	summary = 1.0

	# iterate through nodes
	for i in range(0, len(rna_seq)):
		print ('Base: ', i , rna_seq[i])
		degrees_freedom = 0.0
		temp_var_indices_i = []

		# iterate through all possible base pairs
		for j in range(0, len(basepair_edges)):
			print ('New basepair: ', j)
			# check which tuples contain i and collect their probability
			if i in basepair_edges[j]:
				print(basepair_edges[j])
				# collect these basepairs for later use
				temp_var_indices_i.append(j)
				# calculate number of new branches
				print ('New df : ', probability_of_availability[j])
				degrees_freedom += float(probability_of_availability[j])

		# iterate through all base pairs containing i
		# pdb.set_trace()
		for k in temp_var_indices_i:
			# Adjust the probability of availability
			chance_of_use = probability_of_availability[k]/degrees_freedom
			probability_of_availability[k] = float(1.0 - chance_of_use) 

		if degrees_freedom != 0:
			summary *= degrees_freedom
		# Adjust the answer variable based on this info		
		print('Degrees freedom: ', degrees_freedom, temp_var_indices_i, summary)

	return summary

def counts_perfect_matchings (basepair_edges, rna_seq):
	"""
	Input: List of tuples (all possible basepair bonds), String (rna seq)
	Output: Integer (no. combinations where each base used exactly once)
	"""
	perfect_matches = []
	for i in range(0, len(rna_seq)):
		print('Node: ' , i)
		for j in range(0, len(basepair_edges)):
			if i in basepair_edges:
				perfect_matches[i] = basepair_edges[i]


if __name__ == "__main__":
	rna_seq = single_fasta_to_string(argv[1])
	length_seq = len(rna_seq)
	perfect_matches = length_seq/2
	print(rna_seq, length_seq, perfect_matches)

	basepair_edges = find_base_edges(rna_seq)
	answer = count_perfect_matchings(basepair_edges, rna_seq)
	print('Answer: ', answer, basepair_edges)
#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find no. perfect matchings RNA as per 
http://rosalind.info/problems/cat/
Input: Fasta file path, one RNA seq (num A == num U, same for C-G)
Output: Int, number of perfect matchings
"""

# Standard Libs
from sys import argv
import pdb
import statistics

# My Own External Funcs
from ian_bif_utilities import single_fasta_to_string

# def count_noncross_perf_matches (nodes):
# 	"""
# 	Purpose: Count noncrossing perfect matches
# 	Input: INT nodes the number of nodes in the circular graph
# 	Output: INT total number of non-crossing perfect matches
# 	"""
# 	n = int(nodes/2)
# 	local_total = 0
# 	for m in range(2, nodes+1, 2):
# 		n_left = int((m - 2)/2)
# 		n_right = int((nodes - m)/2)

# 		# For each side of the 1-m bond, count noncross-perf-matches
# 		if n_left == 2:
# 			c_left = 2
# 		elif n_left == 1:
# 			c_left = 1
# 		elif n_left == 0:
# 			c_left = 1
# 		else: c_left = count_noncross_perf_matches(n_left * 2)

# 		if n_right == 2:
# 			c_right = 2 
# 		elif n_right == 1:
# 			c_right = 1 
# 		elif n_right == 0:
# 			c_right = 1 
# 		else: c_right = count_noncross_perf_matches(n_right * 2)
		
# 		local_total += c_left * c_right

# 	return local_total




# def count_noncross_perf_matches (seq):
# 	"""
# 	Purpose: Count noncrossing perfect matches, recursively
# 	Input: INT nodes the number of nodes in the circular graph
# 	Output: INT total number of non-crossing perfect matches
# 	"""
# 	nodes = len(seq)
# 	n = int(nodes/2)
# 	local_total = 0

# 	# potential_Ms = range(len(seq))
# 	for m in range(2, nodes+1, 2):
# 		# m1 = seq[0]
# 		# m2 = seq[m-1]
# 		# Skip to next loop if this match is invalid
# 		if not check_matching_bases(seq[0], seq[m-1]):
# 			continue

# 		# print(m)
# 		# print(seq[0], seq[m-1])
# 		left_seq = seq[1:m-1]
# 		right_seq = seq[m:]
# 		# print (left_seq, right_seq)

# 		# Skip to next loop unless both sides have potentially matching bases
# 		if check_even_bases(left_seq) & check_even_bases(right_seq):
# 			pass
# 		else:
# 			continue

# 		print('seqs: ', left_seq, right_seq)
# 		print(local_total)
# 		n_left = int((m - 2)/2)
# 		n_right = int((nodes - m)/2)

# 		# For each side of the 1-m bond, count noncross-perf-matches
# 		if n_left > 1:
# 			c_left = count_noncross_perf_matches(left_seq)
# 		elif n_left == 1:
# 			c_left = 1
# 		else:
# 			c_left = 1

# 		if n_right > 1:
# 			c_right = count_noncross_perf_matches(right_seq)
# 		elif n_right == 1:
# 			c_right = 1 
# 		else:
# 			c_right = 1 
		
# 		local_total += c_left * c_right

# 	return local_total

def check_even_bases (seq):
	"""
	Check if seq has equal num As as Us and Gs as Cs
	"""
	AU_equal = (seq.count('A') == seq.count('U'))
	GC_equal = (seq.count('G') == seq.count('C'))
	return True if (AU_equal & GC_equal) else False


def check_matching_bases (base1, base2):
	"""
	Check if two bases can pair
	"""
	bases = [base1, base2]
	if ('A' in bases) and ('U' in bases):
		return True
	elif ('G' in bases) and ('C' in bases):
		return True
	else:
		return False


def get_potential_matches (seq):
	"""
	Return a set of indices for which the first element in the seq can base pair
	And for which that base pair will leave both sides with 1:1 for C:G and A:U
	"""
	potential_match_bases = list(range(0, len(seq)))[1::2]
	matches = [x for x in potential_match_bases if check_matching_bases(seq[0], seq[x])]
	matches = [x for x in matches if (check_even_bases(seq[1:x]) and check_even_bases(seq[x+1:])) ]
	return matches

def split_seq(seq):
	"""
	Split the sequence into 4 for parallel computing
	Each must have even number of bases and 1:1 of A:U and C:G
	"""
	# create list of numbers to evenly split seq
	# pop the middle numbers until one has even bases
	# Split the list by this number and export

	splitters = list(range(0, len(seq)))[2::2]
	print(splitters)
	midd = splitters.pop(len(splitters)//2)
	while (not check_even_bases(seq[:midd])) or (not check_even_bases(seq[midd:])):
		midd = splitters.pop(len(splitters)//2)
	print(seq[:midd], seq[midd:])
	return(seq[:midd], seq[midd:])
	# exit()



	# mats = list(range(0, len(seq)))
	# mats = list(range(0, len(seq)))
	# middle = int(len(mats)/2)
	# # pdb.set_trace()
	# # print(seq)
	# # matches = get_potential_matches(seq)
	# # print(matches)
	# # print(mats)
	# # median = statistics.median(mats)
	# # print(median)
	# first_half = seq[:middle-1]
	# second_half = seq[middle:]
	# print([first_half, second_half])
	# return [first_half, second_half]

def count_noncross_perf_matches (seq):
	"""
	Purpose: Count noncrossing perfect matches, recursively
	Input: INT nodes the number of nodes in the circular graph
	Output: INT total number of non-crossing perfect matches
	"""
	nodes = len(seq)
	n = int(nodes/2)
	local_total = 0

	matches = get_potential_matches(seq)
	for m in matches:
		# m1 = seq[0]
		# m2 = seq[m-1]
		# Skip to next loop if this match is invalid
		if not check_matching_bases(seq[0], seq[m]):
			continue

		# print(m)
		# print(seq[0], seq[m-1])
		left_seq = seq[1:m]
		right_seq = seq[m+1:]
		# print (left_seq, right_seq)

		# Skip to next loop unless both sides have potentially matching bases
		if check_even_bases(left_seq) & check_even_bases(right_seq):
			pass
		else:
			continue

		# print('seqs: ', left_seq, right_seq)
		# print(local_total)
		n_left = int((m - 1)/2)
		n_right = int((nodes - (m+1))/2)

		# For each side of the 1-m bond, count noncross-perf-matches
		if n_left > 1:
			c_left = count_noncross_perf_matches(left_seq)
		elif n_left == 1:
			c_left = 1
		else:
			c_left = 1

		if n_right > 1:
			c_right = count_noncross_perf_matches(right_seq)
		elif n_right == 1:
			c_right = 1 
		else:
			c_right = 1 
		
		local_total += c_left * c_right

	return local_total



if __name__ == "__main__":
	seq = single_fasta_to_string(argv[1])	
	# seq = 'AUAUAUCGCGAUAUAUAUAUAU'
	# seq = 'AUAUAU'
	# seq = 'UAUCGACCGAUCAUAUGGGUGCAAUCCCUAUAGCUAGGACGUAUAUAUGCAUAUAUCCCGGGAUAUCGAAUUUA'
	seq = seq.upper()

	# first__half, second_half = split_seq(seq)
	# q1, q2 = split_seq(first__half)
	# q3, q4 = split_seq(second_half)
	# print(q1, '-----', q2,'-----', q3,'-----', q4)
	
	matchings = count_noncross_perf_matches(seq)
	print(matchings)
	exit()

	# # The multiprocessing doesn't work (can't just multiply answers together)
	# from multiprocessing import Pool
	# pool = Pool()
	# result1 = pool.apply_async(count_noncross_perf_matches, [q1]) 
	# result2 = pool.apply_async(count_noncross_perf_matches, [q2]) 
	# result3 = pool.apply_async(count_noncross_perf_matches, [q3]) 
	# result4 = pool.apply_async(count_noncross_perf_matches, [q4])
	# answer1 = result1.get()#timeout=100)
	# answer2 = result2.get()#timeout=100)
	# answer3 = result3.get()#timeout=100)
	# answer4 = result4.get()#timeout=100)
	# print(answer1, answer2, answer3, answer4)

# TODO efficiency --> list instead of strings?
 # --> Start m iteration from middle?


 # 21293710

 # I'm temporarily accepting failure for this one. My code takes hours to run
 # and gives me an anzwer that doesn't look right --> 91725200481245801472000
 # I'll come back to it with a fresh brain, revitalised by success elsewhere
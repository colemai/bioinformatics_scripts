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

# My Own External Funcs
from ian_bif_utilities import single_fasta_to_string

# Functions
# 1. Import the RNA Seq
# 2. Calculate non-cross perfect matchings

# def count_noncross_perf_matches (rseq):
# 	"""
# 	Purpose: Count non crossing perfect matches of a rna seq
# 	Input: STR rna seq <300bp where num A == num U, C == G
# 	Output: INT the number of perfect matchings
# 	"""
# 	print(rseq)
# 	matchings = 0
# 	nodes = len(rseq)
# 	n = nodes/2

# 	# Iterate thu all the nodes that node 1 can bind with (even only)
# 	# For each of these, count the perfect matchings on either side
# 	for m in range(2, nodes+1, 2):
# 		left_matches = count_noncross_perf_matches()
# 		matchings += left_matches * right_matches

# def matches (nodes, total):
# 	# If there are only two nodes, return c2
# 	if nodes % 2 != 0:
# 		print('Warning uneven')

# 	if nodes == 2:
# 		print('Nodes two')
# 		return 1
	
# 	if nodes == 0:
# 		print('Nodes zero')
# 		return 1

# 	# Otherwise split it in two (check all possible splits) 
# 	else: 
# 		# for m in range(2, nodes+1, 2):
# 		m = 4
# 		total += matches(m - 2, total) # left_side
# 		total += matches(nodes - m, total) # right_side

# 	return total

# def matchers(nodes, total):
	
# 	n = nodes/2
# 	for m in range(2, nodes+1, 2):
# 		k = m/2
# 		left = k-1
# 		right = n-k
# 	total += matchers(k-1) * matchers(n-k)


# 	if nodes == 0:
# 		return 1
	
# 	else:
# 		n = nodes/2
# 		for m in range(2, nodes+1, 2):
# 			k = m/2
# 			total += 

# def count_time (nodes):
# 	n = nodes/2
# 	if 
# 	total +=




def matchings (n):
		if n == 2:
			print('n is 2')
			return 2
		if n == 1:
			print('n is 1')
			return 1
		if n == 0:
			print('WARN')
			return 1
		else:
			# Split the remaining nodes in two, multiply
			return (matchings(round(n/2)) * matchings(int(n/2)))

def million (nodes, total):
	n = int(nodes/2)
	local_total = 0
	for m in range(2, nodes+1, 2):
		n_left = int((m - 2)/2)
		n_right = int((nodes - m)/2)
		# pdb.set_trace()
		if n_left == 2:
			print('n left 2')
			c_left = 2
		elif n_left == 1:
			print('n left 1')
			c_left = 1
		elif n_left == 0:
			print('n left 0')
			c_left = 1
		else: c_left = million(n_left * 2, total)

		if n_right == 2:
			print('n right 2')
			c_right = 2 
		elif n_right == 1:
			print('n right 1')
			c_right = 1 
		elif n_right == 0:
			print('n right 0')
			c_right = 1 
		else: c_right = million(n_right * 2, total)
		
		local_total += c_left * c_right
	return local_total
		# print(c_left * c_right)


	# 	c_left = 2 if n_left 
	# 	c_right = 
	# 	if n == 2: 
	# 		total += 2
	# 	else:
	# 		total += million ()


	# if n == 2: 
	# 	total += 
	# for each possible m:
	# 	total += one_half * other_half
	# 	one_half = 1 if n == 1 | 2 if n == 2 | 

if __name__ == "__main__":
	seq = single_fasta_to_string(argv[1])
	total = 0
	totes = million(10, total)
	print(totes)
	# count_noncross_perf_matches(seq1)
	# total = 0
	# total = matches(4, total)	
	# print(total)

	# nodes = len(seq)
	# n = nodes/2
	# total = 0
	# # for i in n:
	# total += matchings(8)
	# print(total)


			
#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Text file with an int (n) on the first line, a permutation of length n
on the second line
Output: The longest possible increasing subsequence followed by the decreasing
Example Call: python3 ros26-lgis.py input.txt
"""

from sys import argv
import pdb

def import_n_perm (file_path):
	"""
	Input: Text file, first line contains an int (n), second line 
	contains a permutation of length n
	Output: int (n), List (alphabet of symbols)
	"""
	with open(file_path) as file_object:
		lines = file_object.readlines()
		perm = lines[1].strip().split(' ')
		perm = [ int(x) for x in perm ]
		n = int(lines[0])
	return n, perm

def longest_subseq_incr (perm):
	"""
	Input: list (permutation)
	Output: list --> longest increasing subsequence of that permutation
	"""
	scores = [1] * len(perm) 
	seqs = [ [x] for x in perm ]

	for i in range(0,len(perm)):
		for j in range(0, len(perm[:i])):
			if perm[i] > perm[j]:
				if scores[j]+1 > scores[i]: seqs[i] =  seqs[j] + [perm[i]]
				scores[i] = max(scores[i], scores[j]+1)		
	
	print(max(scores))
	return max(seqs, key=len)

def longest_subseq_decr (perm):
	"""
	Input: list (permutation)
	Output: list --> longest decreasing subsequence of that permutation
	"""
	scores = [1] * len(perm)
	seqs = [ [x] for x in perm ]

	for i in range(0,len(perm)):
		for j in range(0, len(perm[:i])):
			if perm[i] < perm[j]:
				if scores[j]+1 > scores[i]: seqs[i] =  seqs[j] + [perm[i]]
				scores[i] = max(scores[i], scores[j]+1)		
	
	print(max(scores))
	return max(seqs, key=len)


if __name__ == "__main__":
	n, perm = import_n_perm(argv[1])
	print('n is: ', n)

	longest_incr = longest_subseq_incr(perm)
	longest_decr = longest_subseq_decr(perm)

	# Dumb print formatting
	stringer = ''
	for i in longest_incr:
		stringer += str(i)
		stringer += ' '
	print(stringer)

	stringer = ''
	for i in longest_decr:
		stringer += str(i)
		stringer += ' '
	print(stringer)
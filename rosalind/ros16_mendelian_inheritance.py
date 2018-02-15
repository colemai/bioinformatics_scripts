#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Text file with 3 integers separated by spaces
Output: A probability (float) calculated from input as per challenge

Challenge description: http://rosalind.info/problems/iprb/

"""

from sys import argv
import pdb

def intake_data(file_path):
	"""
	Input: txt file with three ints separated by spaces
	Output: the three ints as a list 
	"""
	with open(file_path) as file_object:
		ints = file_object.read().split(" ")
	return [int(x) for x in ints]

if __name__ == "__main__":
	k,m,nn = intake_data(argv[1])
	total = k + m + nn
	k_probs = k/total + ((nn+m)/total * k/(total -1))
	m_probs = m/total * ((m-1)/(total-1)) 
	m_probs_n = m/total * ((nn)/(total-1))
	n_probs = nn/total * ((m)/(total-1))
	probs = k_probs + (0.75 * m_probs) + (0.5 * m_probs_n) + (0.5 * n_probs)
	print(probs)

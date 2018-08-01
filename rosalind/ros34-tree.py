#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Connect up a tree as per http://rosalind.info/problems/tree/
Input: from txt file --> Int N, series of tuples each on their own line
Output: Minimum number of edges needed to complete the tree described by input
"""

import pdb
from sys import argv

def get_tree_ints (file_path):
	"""
	Input: Txt file path, one int on first line, two on each subsequent
	Output: List of lists of ints, one sub-list per line of ints
	"""
	with open (file_path, 'r') as file_object:
		lines = file_object.readlines()
		lines = [i.strip() for i in lines] # strip 
		lines = [i.split(' ') for i in lines] # split
		lines = [[int(i) for i in j] for j in lines] # convert to int
		return(lines)


if __name__ == "__main__":
	get_tree_ints(argv[1])
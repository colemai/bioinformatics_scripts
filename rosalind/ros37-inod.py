#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Get number of internal nodes in unrooted binary tree given number of leaves as per 
http://rosalind.info/problems/inod/
Input: INT, number of leaves
Output: printed INT, number of internal nodes
"""

from sys import argv
import pdb

if __name__ == "__main__":
	# If there are 3 leaves then there's one internal
	# Else if there are 4 leaves then there are two internal nodes
	# (the internal nodes now need their third edge to connect to each other)
	# If there are 5+ leaves then the two extreme internal nodes each have two children
	# And the internal nodes between them each have one
	leaves = 2022
	if leaves > 4:
		print(leaves - 2) # really didn't need python for this...
		pass
	elif leaves == 3:
		print(1)
	elif leaves == 4:
		print(2)
	else:
		print("Error, should not be {} leaves".format(leaves))

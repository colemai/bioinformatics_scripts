#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A string of AA symbols
Output: A float --> total weight of the given polypeptide (monoisotopic mass, ignoring water molecule)
Example Call: Python3 ros23-prtm.py input-file.txt
"""

from sys import argv
import pdb
import numpy as np

"""
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
"""

def import_string(file_path):
	"""
	Input: Path to text file with single string
	Output: Single string
	"""
	with open(file_path) as file_object:
		lines = file_object.readlines()
		polypeptide = lines[0].strip()
	return polypeptide



if __name__ == "__main__":
	polypeptide = import_string(argv[1])
	print (polypeptide)

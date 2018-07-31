#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Give all signed permutations 
Input: Int (from txt file)
Output: Int (no. signed permutations), then all signed permutations
Briefing: http://rosalind.info/problems/sign/
"""

from sys import argv
import pdb
import numpy as np
from ian_bif_utilities import get_input_ints





if __name__ == "__main__":
	n = get_input_ints(argv[1])[0] #get first and only element from input list
	print(n)
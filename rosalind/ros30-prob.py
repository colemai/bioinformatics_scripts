#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Give probability of exact DNA sequence occuring (given GC content)
Input: String (DNA seq), List (GC contents)
Output: List (Prob of seq for each GC content)
"""

import pdb
from sys import argv

def import_string_and_array (file_path):
    """
    Input: Path to text file with string on first line and list on second
    Output: String, List
    """
    with open(file_path) as file_object:
        lines = file_object.readlines()
        seq = lines[0].strip()
        gc_arr = lines[1].split(' ')
        gc_arr = list(map(lambda x: float(x), gc_arr))
    return seq, gc_arr
    

if __name__ == "__main__":
	seq, gc_arr = import_string_and_array(argv[1])
	print(seq, gc_arr)
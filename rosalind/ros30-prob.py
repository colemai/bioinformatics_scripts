#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Give probability of exact DNA sequence occuring (given GC content)
Input: String (DNA seq), List (GC contents)
Output: List (Prob of seq for each GC content)
"""

import pdb
import math
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

def probability_seq_occurring (seq, gc_content):
	"""
	Input: String (DNA sequence), float (gc content)
	Output: Float (probability of that exact sequence occuring)
	"""
	prob_g_c = gc_content / 2
	prob_a_t = (1 - gc_content) / 2
	prob_dict = {'A': prob_a_t, 'C': prob_g_c, 'G': prob_g_c, 'T': prob_a_t}

	final_prob = 1
	for base in seq:
		final_prob *= prob_dict[base]
	return final_prob

def prob_seq_occuring_for_multiple_gc_contents (seq, gc_arr):
	"""
	REQUIRES probability_seq_occuring !!!
	Input: String (seq), list (gc contents)
	Output: List of floats (probabiltiy seq occuring per gc_content)
	"""
	final_probabilities = []
	for gc_content in gc_arr:
		final_probabilities.append(probability_seq_occurring(seq,gc_content))
	return final_probabilities


if __name__ == "__main__":
	seq, gc_arr = import_string_and_array(argv[1])
	final_probs = prob_seq_occuring_for_multiple_gc_contents (seq, gc_arr)
	
	# Apply common log
	final_probs_logs = list(map(lambda x: math.log10(x), final_probs))

	for value in final_probs_logs:
		print("{:.3f}".format(value))
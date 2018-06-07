#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A txt file with 6 integers (corresponding to no. couples with 
a genotype pair)
Output: Single integer - Expected value (long term average prob) of no. offspring
with dominant output

Challenge description: http://rosalind.info/problems/iev/
"""

from sys import argv
import pdb
import numpy as np

def get_input_txt(txt_path):
	"""
	Input: path to txt file with multiple ints
	Output: list of ints
	"""
	with open(txt_path, 'r') as txt:
		line = txt.read()
		line = np.asarray(line.split(' ')) # convert input to numpy array
		line = line.astype(np.int) # convert from str to ints
	return line

def expected_val_dom_phenotype(couples_genotypes):
	"""
	Input: np array of couples genotypes (6 ints)
	Output: expected value of dominant phenotype (as an int)
	
	Genotype combos:
	AA-AA
	AA-Aa
	AA-aa
	Aa-Aa
	Aa-aa
	aa-aa
	"""

	#Establish dictionary to convert each combo (above) to its probability of dominant phenotype
	probability = np.asarray([1,1,1,0.75,0.5,0])
	offspring = couples_genotypes * 2 # as each pair has 2 offspring
	
	predicted_phenotypes = offspring * probability
	
	expected_value = np.sum(predicted_phenotypes)
	print(expected_value)

if __name__ == "__main__":
	couples_genotypes = get_input_txt(argv[1])
	expected_val_dom_phenotype(couples_genotypes)
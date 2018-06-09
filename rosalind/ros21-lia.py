#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Two integers k (generation) and N (number of Aa Bb genotypes to check for in k)
Output: A Float --> probability of N Aa Bb genotypes in generation k

Challenge description: http://rosalind.info/problems/lia/

"""

from sys import argv
import numpy as np 
import pdb

def get_input_ints(txt_path):
	"""
	Input: path to txt file with multiple ints
	Output: np array of ints
	"""
	with open(txt_path, 'r') as txt:
		line = txt.read()
		line = np.asarray(line.split(' ')) # convert input to numpy array
		line = line.astype(np.int) # convert from str to ints
	return line

def genotype_probabilities(k):
	"""
	Input: integer k (generation) 
	Output: A list --> probability of genotypes [p(AA),p(Aa), p(aa)]
	"""
	current_generation = [0,1,0] #,0,1,0]
	punnettAA = [0.5,0.5,0]
	punnettAa = [.25,.5,.25]
	punnettaa = [0, 0.5, 0.5]

	for i in range(1,k+1):
		print ('gen ', i)
		next_generation = current_generation[:]
		for j in range(0,len(current_generation)):
			next_generation[j] = (current_generation[0] * punnettAA[j]) + (current_generation[1] * punnettAa[j]) + (current_generation[2] * punnettaa[j])
		current_generation = next_generation[:]
		print (current_generation)
	print('final genotype ', current_generation)
	return(current_generation)



def AaBb_prob(genotypes, N, k):
	"""
	Input: A list --> [p(AA),p(Aa), p(aa)] and int N (number of Aa Bb genotypes to check for in k), int k
	Output: A Float --> probability of N Aa Bb genotypes in generation k
	"""
	print(genotypes,N)
	population = 2**k
	individual_prob_AaBb = genotypes[1] ** 2
	individual_prob_other = 1 - individual_prob_AaBb

	number_to_disprove = (population-N) + 1
	prob_false = (individual_prob_other ** number_to_disprove) 
	prob_true = 1 - prob_false
	pdb.set_trace()
	return prob_true

if __name__ == "__main__":
	k,n = get_input_ints(argv[1])
	# print(k,n)
	probabilities = genotype_probabilities(k)
	answer = AaBb_prob(probabilities,n, k)
	print(answer)


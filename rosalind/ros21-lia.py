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
	genotype_probs = [0,1,0] #,0,1,0]
	punnettAA = [0.5,0.5,0]
	punnettAa = [.25,.5,.25]
	punnettaa = [0, 0.5, 0.5]

	for i in range(1,k+1):
		print ('gen ', i)
		for j in range(0,len(genotype_probs)):
			genotype_probs[j] = (genotype_probs[0] * punnettAA[j]) + (genotype_probs[1] * punnettAa[j]) + (genotype_probs[2] * punnettaa[j])
			# generation[j] = generation[j] * prob
		print (genotype_probs)
	print('final genotype ', genotype_probs)
	return(genotype_probs)

def AaBb_prob(genotypes, N, k):
	"""
	Input: A list --> [p(AA),p(Aa), p(aa)] and int N (number of Aa Bb genotypes to check for in k), int k
	Output: A Float --> probability of N Aa Bb genotypes in generation k
	"""
	print(genotypes,N)
	population = k * 2
	individual_prob_AaBb = genotypes[1] ** 2
	individual_prob_other = 1 - individual_prob_AaBb

	number_to_disprove = (population-N) + 1
	pdb.set_trace()
	return(individual_prob_other ** number_to_disprove)


	# [0.28125, 0.53125, 0.2109375, 0.28125, 0.53125, 0.2109375]
	# pop = k* 2
	# prob of at least N of k having Aa 
	# = 1 - (prob of (k-n) + 1 not having Aa)
	# = prob of not having Aa = 1 - genotype_probs[1]
	# = notAa^(k-n) +1
	# prob of at least N of k having Bb 

	# prob of both:

	# place 0 = probsAA 
	# generation[0] = generation[0] * probsAA[0] + generation[1] * probsAa[0] + generation[2] * probsaa[0]


if __name__ == "__main__":
	k,n = get_input_ints(argv[1])
	# print(k,n)
	probabilities = genotype_probabilities(k)
	answer = AaBb_prob(probabilities,n, k)
	print(answer)




 #  A  a
 # A AA Aa

 # a aA aa


  #  A  A
  # AAA AA

  # aAa Aa

 # lister = [numpeople, p(AA),p(Aa),p(aa),p(BB),p(Bb),p(bb)]
 # probsAA = [p(AA),p(Aa), p(aa)]
 # probsAA = [0.5,0.5,0]
 # probsAa = [.25,.5,.25]
 # probsaa = [0, 0.5, 0.5]
# 0,1,0,       0,1,0
# .25,.5,.25   .25,.5,.25


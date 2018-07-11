#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Find partial permutations as per http://rosalind.info/problems/pper/
Input: Path to txt file, two ints on one line separated by a space
Output: Int (number of permutations of k out of n elements)
"""

from sys import argv
import pdb
import math

def get_ints_from_file (file_path):
	"""
	Returns two ints from txt file with two ints on one line
	"""
	with open(file_path) as file_object:
		line = file_object.read()
		n,k = line.split(' ')
		n = int(n)
		k = int(k)
	return n,k

 
def factorial (n):
    return 1 if (n < 1) else n * factorial(n-1)

def combinations (n, r):
	return factorial(n)/(factorial(r) * factorial(n-r))


if __name__ == "__main__":
	n,k = get_ints_from_file(argv[1])
	print('n: ', n, 'k: ', k)

	combinations = combinations(n,k)
	factorial_k = factorial(k)

	print('ANS: ', (factorial_k * combinations) % 1000000)
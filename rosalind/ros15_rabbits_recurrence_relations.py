#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: Text file of two ints separated by a space

Challenge: 
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset
5 3
Sample Output
19

"""

from sys import argv
import pdb

def intake_data(text_file):
	"""
	Input: text file with two integers (n and k) separated by a space
	Output: two ints: n, k 
	""" 
	with open(text_file) as file_object:
		full_input = file_object.read()
		split_input = full_input.split(" ")
	return int(split_input[0]), int(split_input[1])

def number_rabbits(n, k):
	"""
	Input: Two ints, n the no. months, k the no. offspring pairs per breeding
	Output: Resulting no. rabbits after n months
	"""
	seq = [1, 1]
	if n <= 2: return seq[n]
	
	#Cycle through each month until nth month, appending total pairs
	for i in range(2, n):
		new_pairs = seq[i-1] + (k *seq[i-2])
		seq.append(new_pairs)
	return seq[n-1] 

if __name__ == "__main__":
	n,k = intake_data(argv[1])
	answer = number_rabbits(n,k)
	print(answer)


#Recurrence relation: Fn = Fn-1 + k(Fn-2)
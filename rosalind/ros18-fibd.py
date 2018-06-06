#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: A txt file with two integers (end_point and longevity)
Output: An integer (number of rabbits at end_point)

Challenge description: http://rosalind.info/problems/fibd/

"""

from sys import argv
import pdb

def get_input_txt(txt_path):
	"""
	Input: path to txt file with two ints
	Output: two ints
	"""
	with open(txt_path, 'r') as txt:
		line = txt.read()
		end_time, longevity = line.split(' ')
	return int(end_time), int(longevity)

def rabbit_population_predictor(end_time, longevity):
	"""
	Input: Month at which to measure pop (end_time, int) and longevity of rabbits in months (longevity, int)
	Output: Predicted number of rabbits at a given time (int)
	"""
	
	# Record current population and also new births in separate dictionaries
	rabbit_census = {0: 0, 1: 1}
	birth_record = {0: 0, 1:1}

	# Iterate through each month and calculate births, deaths, resulting population
	for month_to_calc in range(2, end_time + 1):
		death_toll = 0
		if month_to_calc > longevity:
			death_toll = birth_record[month_to_calc - longevity]
		immature = birth_record[month_to_calc -1]
		breeding_pairs = rabbit_census[month_to_calc -1] - immature
		resulting_pop = rabbit_census[month_to_calc -1] + breeding_pairs - death_toll

		# Update the dictionaries with the values for this month
		rabbit_census[month_to_calc] = resulting_pop
		birth_record[month_to_calc] = breeding_pairs

	return(rabbit_census[end_time])


if __name__ == "__main__":
	end_time, longevity = get_input_txt(argv[1])
	answer = rabbit_population_predictor(end_time, longevity)
	print(answer)

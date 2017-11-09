#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose:
"""

from sys import argv

def intake_fastq (input_file):
    """Yield lines from a single record of file (fastq format)

    lines: list of lines or open file object
    """
    with open(input_file, 'r') as fastq:
    	fastq_list = fastq.readlines()
    	return fastq_list

def record_finder_2(lines):
	record_number = 0
	entry_number = 0
	master_list = []
	temp_list = []
	for i in range(0, len(lines)):
		if entry_number == 0:
			temp_list.append(lines[i].strip())
			entry_number += 1
		elif entry_number == 1 or entry_number == 2:
			temp_list.append(lines[i].strip())
			entry_number += 1
		elif entry_number == 3:
			temp_list.append(lines[i].strip())
			entry_number = 0
			record_number += 1
			master_list.append(temp_list)
			temp_list = []
	return(master_list)

# def mmake_dict(input_list):
# 	seqdict=dict()
# 	for i in input_list:
# 		label = i[0]
# 		sequence = i[1]
# 		quality = i[3]
# 		seqdict[label] = {'Sequence':sequence, 'Quality': quality}
# 	print(seqdict['@FCC0U42ACXX:2:1101:17553:4175#ACTACAAG/1'])

def make_list(input_list):
	seqlist=[]
	for i in input_list:
		seq_dict = {}
		seq_dict['label'] = i[0]
		seq_dict['sequence'] = i[1]
		seq_dict['quality'] = i[3]
		seqlist.append(seq_dict)
	return seqlist

def get_quals(listed_fastq):
	for i in listed_fastq:
		quality_list = []
		for index in i['quality']:
			quality_list.append(ord(index) - 64)
		i['quality_int'] = quality_list
	return listed_fastq

def get_lengths(listed_fastq):
	lengths = []
	for i in listed_fastq:
		i['sequence_length'] = len(i['sequence'])
		lengths.append(len(i['sequence']))
	length_stats ={'min': min(lengths), 'max':max(lengths), 'mean': sum(lengths)/len(lengths)}
	return length_stats

def mean_quals(listed_fastq, length_stats):
	mean_qual_list = []
	for index in range(0,length_stats['max']):
		qual_at_position = []
		for entry in listed_fastq:
			qual_at_position.append(entry['quality_int'][index])
		mean_qual_list.append(sum(qual_at_position)/len(qual_at_position))
	print (mean_qual_list)

if __name__ == "__main__":
	fastq_lines = intake_fastq(argv[1])
	fastq_lines_2 = record_finder_2(fastq_lines)
	listed_fastq = make_list(fastq_lines_2)
	listed_fastq_2 = get_quals(listed_fastq)
	length_stats = get_lengths(listed_fastq_2)
	mean_quality_list = mean_quals(listed_fastq_2, length_stats)
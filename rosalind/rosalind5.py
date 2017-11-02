#!/usr/bin/python3

from sys import argv

def parse_input (input_filename):
	with open(input_filename, 'r') as file_object:
		first_line =file_object.readline().strip()
		print (first_line)


#def fasta_entry_splitter

#def fasta_label_splitter



parse_input(argv[1])
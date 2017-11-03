#!/usr/bin/python3

from sys import argv
fasta = ''

def parse_fasta (input_filename):
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        fasta_dict = {}
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                label_index = file_list[i].strip()
                fasta_dict[file_list[i].strip()] = ''
            else: 
                fasta_dict[label_index] += file_list[i].strip()
        print (fasta_dict)
        
        

#def fasta_entry_splitter

#def fasta_label_splitter



parse_fasta(argv[1])


#!/usr/bin/python3

from sys import argv

def parse_fasta (input_filename):
    #Converts fasta file into a dictionary. Input of fasta file.
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        fasta_dict = {}
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                label_index = file_list[i].strip()
                fasta_dict[file_list[i].strip()] = ''
            else: 
                fasta_dict[label_index] += file_list[i].strip()
        return fasta_dict




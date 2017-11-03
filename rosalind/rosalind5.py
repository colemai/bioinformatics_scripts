#!/usr/bin/python3
"""
author: Ian Coleman
purpose: output label and gc content of seq with highest gc content of seqs in a fasta file
"""

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
    
def gc_content_fasta (input_fasta):
    #iterate thru fasta dict, add each key to new_dict, calculate \
    #each val'sgc content % and make this the val in new_dict
    output_list = [0, 0]
    for key, value in input_fasta.items():
        #calculate gc content of strings here
        
        if value > output_list[1]:
            output_list[0] = key
            output_list[1] = value
    #this seems unnecessarily heavy computationally. Better to ? organise
        

#if __name__ == "__main__":


fasta_dict = parse_fasta(argv[1])
gc_content_fasta(fasta_dict)




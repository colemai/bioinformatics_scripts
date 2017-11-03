#!/usr/bin/python3

from sys import argv
fasta = ''

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
    output_dict = {}
    for key, value in input_fasta.items():
        output_dict[key] = 0
        print(value)
        

#if __name__ == "__main__":


fasta_dict = parse_fasta(argv[1])
gc_content_fasta(fasta_dict)




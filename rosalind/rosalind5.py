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
        #iterate through each line, add label as key and sequence as value
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                label_index = file_list[i].strip()
                fasta_dict[file_list[i].strip()] = ''
            else: 
                fasta_dict[label_index] += file_list[i].strip()
        return fasta_dict
    
def gc_content_fasta (input_fasta):
    #Take input of fasta dict, output the label and gc % of seq with highest gc %
    output_list = [0, 0]
    for label, sequence in input_fasta.items():
        #calculate gc content % of this sequence
        gc_proportion = (sequence.count('C') + sequence.count('G'))/len(sequence) * 100
        
        #if this gc content is the highest yet, make it the new output 
        if gc_proportion > output_list[1]:
            output_list[0] = label
            output_list[1] = gc_proportion
        #this last part seems unnecessarily heavy computationally. Better to sort?
    print (output_list[0][1:])
    print (output_list[1])


if __name__ == "__main__":
    #run the methods
    fasta_dict = parse_fasta(argv[1])
    gc_content_fasta(fasta_dict)




#!/usr/bin/python3
"""
author: Ian Coleman
purpose: Calculate Hamming Distance between two NT seqs
input: text file with two lines, a seq on each
output: single int, the Hamming distance i.e minimum point mutations between seqs
"""

from sys import argv

def intake_seqs (input_filename):
    #Converts fasta file into a dictionary. Input of fasta file.
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        #iterate through each line, add label as key and sequence as value
        seqs = [file_list[0].strip(), file_list[1].strip()]
    
    hamming = 0
    for i in range(0, len(seqs[1])):
        if seqs[1][i] == 'T': 
            if seqs[0][i] == 'T': pass
            else: hamming +=1
        elif seqs[1][i] == 'A': 
            if seqs[0][i] == 'A': pass
            else: hamming +=1
        elif seqs[1][i] == 'C': 
            if seqs[0][i] == 'C': pass
            else: hamming +=1
        elif seqs[1][i] == 'G': 
            if seqs[0][i] == 'G': pass
            else: hamming +=1
    print (hamming)

if __name__ == "__main__":
    #run the methods
    intake_seqs(argv[1])





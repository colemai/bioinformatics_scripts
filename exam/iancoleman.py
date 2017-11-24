#!/usr/bin/python3
"""
Author: Ian Coleman
Student Number: 910616160090

"""

from sys import argv
import subprocess
import re
import os

# STEP1 Read the filenames of the GFF file and the FASTA file with reference proteins
# from the command line (using argv)

def parse_fasta (input_filename):
    """
    Input: Fasta File
    Output: Dictionary of {label: sequence} both strings
    """
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

def parse_gff (input_filename):
    """
    Input: GFF File
    Output: List of tuples [(gene number, protein seq)]
    """
    with open(input_filename, 'r') as file_object:
        file_list = file_object.read()
        processed_file = re.sub(r"\W", "", file_list)
        gene_list = []
        gene_number = 1
        starting_index = processed_file.find("proteinsequence")
        protein_sequences = re.finditer('[A-Z]+', processed_file[starting_index:])
        for sequence in protein_sequences:
            if (sequence.group(0).strip() != "AUGUSTUS") and (sequence.group(0).strip() != "CDS")\
            and (sequence.group(0).strip() != "AUGUSTUSCDS"):
                gene_list.append((gene_number, sequence.group(0)))
                gene_number += 1
        return gene_list

def protein_list_to_fasta (protein_list, out_file):
    """
    Input: List of tuples [()], string name for output file
    Output: Returns nothing, creates fasta file of name out_file
    """
    if os.path.exists(out_file):
        return out_file
    with open(out_file, 'w') as out:
        for gene,sequence in protein_list:
            out.write('>Gene g' + str(gene) + '\n')
            out.write(sequence + '\n')

reference = parse_fasta(argv[1])
gff = parse_gff(argv[2])
protein_list_to_fasta(gff, 'predicted_proteins.fasta')


#Step2 In your script, extract the predicted protein sequences and store them in a fasta
#file (predicted.fasta)


#Step3 In your python script, run the programs makeblastdb and blastp to compare
# the predicted proteins (predicted.fasta) as query to the reference proteins
#(yeast_proteins.fa) as database.
# Set the output format in blastp to 7 (tabular)
# Store only the first hit (set number of alignments to 1)
# Call the blastp output file yeast.blast
 
#Step4 Parse the resulting blast output to extract the relevant information

#Step5 Write code to calculate the percent query coverage as (the length of the aligned
#part of the query/ total query length)*100

#Step7 Create a tab-delimited table with the query ID, query length, subject ID of the
#blast hit, percent identity of the hit (printed with 2 decimals), and the query
#coverage (printed with 2 decimals). 




#Step1 Read in both reference and assembly files
def parse_fasta (input_filename):
    """
    Input: Fasta File
    Output: Dictionary of {label: sequence} both strings
    """
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


def run_cmd(argv):
     """Returns the name of the input file from argv
     
     Keyword arguments:
     argv -- list, command-line arguments
     Returns:
     file_name -- string, name of file provided as argument
     """

     # check if output file already exists
     if os.path.exists(out_file):
        return out_file

# if __name__ == "__main__":

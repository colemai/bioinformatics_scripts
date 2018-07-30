#!/usr/bin/python3
"""
Author: Ian Coleman
Student Number: 910616160090

Run a blast comparison of a gff file (query) and a fasta file (reference)
"""
from sys import argv
import subprocess
import re
import os

# STEP1 Read in a GFF file and a FASTA file with reference proteins
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

#Step2 Extract the predicted protein sequences and store them in a fasta file
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

#Step3 Run the programs makeblastdb and blastp to compare the predicted proteins to reference

def blast ():
    """
    Input: reference fasta, query fasta
    Output: 
    """
    out_file = 'yeast.blast'
    if os.path.exists(out_file):
        return out_file
    cmd_make_db = "makeblastdb -in yeast_proteins.fa -input_type 'fasta' -dbtype 'prot'"
    cmd_blast = "blastp -query predicted_proteins.fasta -db yeast_proteins.fa -outfmt 7 -out \
    {} -num_alignments 1".format(out_file)
    subprocess.check_call(cmd_make_db, shell=True)
    subprocess.check_call(cmd_blast, shell=True)

 
#Step4 Parse the resulting blast output 
def blast_parser (blast_file):
    """
    Input: A blast file name in current dir (or with relative path)
    Output: Master dict of blast
    """
    master_blast = {}
    with open(blast_file) as file_object:
        file_list = file_object.read().split('# BLASTP 2.6.0+')
        for line in range(1, len(file_list) -1):
            this_line = file_list[line].replace('# ', '').strip()
            this_line = this_line.split('\n')
            query_id = this_line[0].split(': ')[1].split(' ')[-1]
            values = this_line[-1].split('\t')
            query_length = int(values[7]) 
            query_identity = float(values[2])
            alignment_length = int(values[3])
            seq_id = values[1]
            coverage = ((alignment_length/query_length) * 100)
            master_blast[query_id] = {'Query_length': query_length, 'Query_identity':query_identity,\
            'qcov': coverage, 'seqid': seq_id}
    return master_blast

    # query = {query_id: x, query_length, }


if __name__ == "__main__":
    reference = parse_fasta(argv[1])
    gff = parse_gff(argv[2])
    protein_list_to_fasta(gff, 'predicted_proteins.fasta')
    blast()
    blast_results = blast_parser('yeast.blast')

    #print out the results in a tab delimited format
    print ('qseqid' + '\t' + 'qlength' + '\t' +  'sseqid' + '\t' + 'pident' + \
            '\t' + 'qcov')
    for key, value in blast_results.items():
        print (key + '\t' + str(value['Query_length']) + '\t' + str(value['seqid'])\
            + '\t' + str(value['Query_identity']) + '\t' + str(value['qcov']))



    #TODO uncomment blast and either remove all args and params or
    #make the args be correct names
    #Change docstrings to pep27 or whatever
    #Add comments and remove comments
    #Ensure lines aren't over line limit length as per pep257
    #Assertions
    #Optimsie parse_gff

